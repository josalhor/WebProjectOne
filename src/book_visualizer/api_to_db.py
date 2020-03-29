
from . import api_entrypoints
from . import models
from datetime import date

def check_isbn(isbn):
    if models.Book.objects.filter(pk=isbn).exists():
        return
    
    json = api_entrypoints.best_sellers_history(isbn=isbn)
    if json is None:
        return
    for result in json['results']:
        for isbns in result['isbns']:
            if isbn == isbns['isbn13']:
                image = result['book_image'] if 'book_image' in result else None
                models.Book.objects.update_or_create(
                    isbn = isbn,
                    price = result['price'],
                    image = image,
                    author = result['author'],
                    published_date = result['published_date'],
                    publisher = result['publisher'],
                    summary = result['description']
                )
                return

def check_book_name(name):
    json = api_entrypoints.best_sellers_history(title=name)
    if json is None:
        return
    if isinstance(json['results'], list):
        for result in json['results']:
            image = result['book_image'] if 'book_image' in result else None
            models.Book.objects.update_or_create(
                isbn = result['isbns'][0]['isbn13'],
                price = result['price'],
                image = image,
                author = result['author'],
                published_date = result['published_date'],
                publisher = result['publisher'],
                summary = result['description']
            )
    else:
        result = json['results']
        image = result['book_image'] if 'book_image' in result else None
        models.Book.objects.update_or_create(
            isbn = result['isbns'][0]['isbn13'],
            price = result['price'],
            image = image,
            author = result['author'],
            published_date = result['published_date'],
            publisher = result['publisher'],
            summary = result['description']
        )

def update_list_names():
    json = api_entrypoints.best_sellers_names()
    if json is None:
        return
    
    for result in json['results']:
        models.BestSellersListName.objects.update_or_create(
            name=result['list_name'],
            display_name=result['display_name'],
            list_name_encoded=result['list_name_encoded']
        )

def update_best_sellers():
    latest = models.BestSellers.objects.order_by('-day').first()
    if latest is not None and latest.day == date.today():
        return

    for l in models.BestSellersListName.objects.all():
        json = api_entrypoints.best_sellers_lists_by_date(list=l.list_name_encoded)
        if json is None:
            continue
        if isinstance(json['results'], list):
            for result in json['results']:
                image = result['book_image'] if 'book_image' in result else None
                models.Book.objects.update_or_create(
                    isbn = result['isbns'][0]['isbn13'],
                    price = result['price'],
                    image = image,
                    author = result['author'],
                    published_date = result['published_date'],
                    publisher = result['publisher'],
                    summary = result['description']
                )
        else:
            result = json['results']
            image = result['book_image'] if 'book_image' in result else None
            models.Book.objects.update_or_create(
                isbn = result['isbns'][0]['isbn13'],
                price = result['price'],
                image = image,
                author = result['author'],
                published_date = result['published_date'],
                publisher = result['publisher'],
                summary = result['description']
            )