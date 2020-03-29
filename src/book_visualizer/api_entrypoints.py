import requests
import time
import os
from datetime import date
from pprint import pprint

def best_sellers_lists(list, bestsellers_date=None, published_date=None, offset=None):
    """Gets the Best Sellers list

    Parameters:
    list (string): The name of the Times best sellers list. 

    bestsellers_date (date): The week-ending date for the sales reflected on list-name.

    published_date (date): The date the best sellers list was published on NYTimes.com.

    offset (int): Sets the starting point of the result set. Must be a multiple of 20.

    """
    key = os.environ.get('NYT_API_KEY')
    url = "https://api.nytimes.com/svc/books/v3/lists/"+list+".json?api-key="+key
    if bestsellers_date is not None:
        url += "&bestsellers-date="+date_to_str(bestsellers_date)
    if published_date is not None:
        url += "&published-date="+date_to_str(published_date)
    if offset is not None:
        url += "&offset="+str(offset)
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        return results
    else:
        print ("Error code %s" %response.status_code)
        return None

def best_sellers_lists_by_date(list, date=None, offset=None):
    """Gets the Best Sellers list by date

    Parameters:
    list (string): The name of the Times best sellers list. 

    bestsellers_date (date): The week-ending date for the sales reflected on list-name.

    offset (int): Sets the starting point of the result set. Must be a multiple of 20.

    """
    key = os.environ.get('NYT_API_KEY')
    date = date_to_str(date)
    url = "https://api.nytimes.com/svc/books/v3/lists/"+date+"/"+list+".json?api-key="+key
    if offset is not None:
        url += "&offset="+str(offset)
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        return results
    else:
        print ("Error code %s" %response.status_code)
        return None

def best_sellers_history(age_group=None, author=None, contributor=None, isbn=None, offset=None, price=None, publisher=None, title=None):
    """Gets the Best Sellers list history

    Parameters:
    age_group (string): The target age group for the best seller.

    author (string): The author of the best seller.

    contributor (string): The author of the best seller, as well as other contributors such as the illustrator.

    isbn (string): International Standard Book Number, 10 or 13 digits

    offset (int): Sets the starting point of the result set. Must be a multiple of 20.

    price (string): The publisher's list price of the best seller, including decimal point.

    publisher (string): The standardized name of the publisher.

    title (string): The title of the best seller.

    """
    key = os.environ.get('NYT_API_KEY')
    url = "https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key="+key
    if age_group is not None:
        url += "&age-group="+str(age_group)
    if author is not None:
        url += "&author="+str(author)
    if contributor is not None:
        url += "&contributor="+str(contributor)
    if isbn is not None:
        url += "&isbn="+str(isbn)
    if offset is not None:
        url += "&offset="+str(offset)
    if price is not None:
        url += "&price="+str(price)
    if publisher is not None:
        url += "&publisher="+str(publisher)
    if title is not None:
        url += "&title="+str(title)
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        return results
    else:
        print ("Error code %s" %response.status_code)

def best_sellers_names():
    """Gets the Best Sellers list names

    """
    key = os.environ.get('NYT_API_KEY')
    url = "https://api.nytimes.com/svc/books/v3/lists/names.json?api-key="+key
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        return results
    else:
        print ("Error code %s" %response.status_code)
        return None

def top_five_best_sellers_with_date(published_date=None):
    """Gets top five books for all the Best Sellers lists for specified date.

    Parameters:

    published_date (date): The best-seller list publication date.

    """
    key = os.environ.get('NYT_API_KEY')
    url = "https://api.nytimes.com/svc/books/v3/lists/overview/.json?api-key="+key
    if published_date is not None:
        url += "&published-date="+date_to_str(published_date)
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        return results
    else:
        print ("Error code %s" %response.status_code)
        return None

def reviews(isbn=None, title=None, author=None):
    """Gets book reviews

    Parameters:
    isbn (string): International Standard Book Number, 10 or 13 digits.
    
    title (string): The title of the best seller.
    
    author (string): The author of the best seller.

    """
    key = os.environ.get('NYT_API_KEY')
    url = "https://api.nytimes.com/svc/books/v3/reviews/9781524763138.json?api-key="+key
    if isbn is not None:
        url += "&isbn="+str(isbn)
    if title is not None:
        url += "&title="+str(title)
    if author is not None:
        url += "&author="+str(author)
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        return results
    else:
        print ("Error code %s" %response.status_code)
        return None

def date_to_str(date):
    """Returns a string representing the date given.

    Parameters:
    date (date): The date to convert.

    """
    key = os.environ.get('NYT_API_KEY')
    if date is None:
        return "current"
    date_str=date.strftime("%Y-%m-%d")
    return date_str

if __name__== "__main__":
    best_sellers_lists("hardcover-fiction")
    best_sellers_lists_by_date("hardcover-fiction", date(2015,3,30))
    best_sellers_history()
    best_sellers_names()
    top_five_best_sellers_with_date()
    reviews()