
from . import api_entrypoints
from . import models
from datetime import date

# def check_isbn(isbn):
#     if models.Book.objects.filter(pk=isbn).exists():
#         return
    
#     json = api_entrypoints.best_sellers_history(isbn=isbn)
#     if json is None:
#         return
#     for result in json['results']:
#         for isbns in result['isbns']:
#             if isbn == isbns['isbn13']:
#                 models.Book.objects.update_or_create(
#                     isbn = isbn,
#                     author = result['author'],
#                     published_date = result['published_date'],
#                     publisher = result['publisher'],
#                     summary = result['description']
#                 )
#                 return

# def check_book_name(name):
#     json = api_entrypoints.best_sellers_history(title=name)
#     if json is None:
#         return
#     if isinstance(json['results'], list):
#         for result in json['results']:
#             models.Book.objects.update_or_create(
#                 isbn = result['primary_isbn10'],
#                 author = result['author'],
#                 published_date = result['published_date'],
#                 publisher = result['publisher'],
#                 summary = result['description']
#             )
#     else:
#         result = json['results']
#         models.Book.objects.update_or_create(
#             isbn = result['primary_isbn10'],
#             author = result['author'],
#             published_date = result['published_date'],
#             publisher = result['publisher'],
#             summary = result['description']
#         )

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

def update_best_sellers_list(l):
    latest = models.BestSellers.objects.filter(list_name=l).order_by('-day').first()
    if latest is not None and latest.day == date.today():
        return False
    json = api_entrypoints.best_sellers_lists_by_date(list=l.list_name_encoded)
    if json is None:
        return False
    best_sellers = models.BestSellers(day=date.today(), list_name=l)
    best_sellers.save()
    for result in json['results']['books']:
        isbn = result['primary_isbn13'] if result['primary_isbn13'] is not None else result['primary_isbn10']
        if 13 < len(isbn):
            continue # we should investigate this further
        defaults = {
            'isbn': isbn,
            'title': result['title'],
            'author': result['author'],
            'bestsellers_date': json['results']['bestsellers_date'],
            'publisher': result['publisher'],
            'summary': result['description']
        }
        book, _ = models.Book.objects.update_or_create(
            defaults,
            isbn = isbn
        )
        best_sellers.books.add(book)
    return True

def update_best_sellers():
    for l in models.BestSellersListName.objects.all():
        updated = update_best_sellers_list(l)
        if not updated:
            return