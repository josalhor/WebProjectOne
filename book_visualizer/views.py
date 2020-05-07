from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreationForm, ContactForm, UserChangeForm, UserForm
from .models import Book, BestSellersListName, BestSellers, Comment, User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError

from rest_framework import viewsets

from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from . import api_to_db, serializers, permissions

from random import shuffle

class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'sign_up.html'


def get_random_categories():
	categories = list(BestSellersListName.objects.all())
	shuffle(categories)
	return categories[:10]

# We are using reverse_lazy because for all generic class-based views the urls
# are not loaded when the file is imported, so we have to use the lazy form of
# reverse to load them later when they are available.

def bestsellers_list(request):
	api_to_db.update_best_sellers()
	books = Book.objects.all()
	categories = get_random_categories()
	page = request.GET.get('page', 1)

	paginator = Paginator(books, 6) # Show 6 books per page
	try:
		bestsellers = paginator.page(page)
	except PageNotAnInteger:
		bestsellers = paginator.page(1)
	except EmptyPage:
		bestsellers = paginator.page(paginator.num_pages)
	
	context = {
		'bestsellers': bestsellers,
		'categories': categories
	}

	return render(request, 'home.html', context)

def book_details(request, pk):
	"""Filters books by ISBN.

	Parameters:
	request (request): Browser request for the view.

	pk (isbn): International Standard Book Number, 10 or 13 digits.

	"""
	book = Book.objects.get(pk=pk)
	comments = Comment.objects.all().filter(based_on = book).order_by('-date')
	num_comments = 0
	num_comments_user = 0
	average  = 0
	num_stars = 0
	wished_books = -1
	added_book = False
	for comment in comments:
		average = average + int(comment.stars)
		num_comments = num_comments + 1
	if num_comments == 0:
		average = 0
	else:
		average = average / (num_comments)
		average = round(average, 2)

	num_stars = round(average)
	
	if request.user.is_authenticated:
		num_comments_user = Comment.objects.filter(made_by=request.user, based_on=book).count()
		u = User.objects.get(username=request.user)
		wished_books = u.whishes.all()
		if(wished_books.filter(pk=pk).count() == 1): added_book = True


	context = {
		'book': book,
		'num_comments': num_comments,
		'num_comments_user': num_comments_user,
		'comments': comments,
		'average': average,
		'num_stars': num_stars,
		'wished_books': wished_books,
		'added_book': added_book
	}

	return render(request, 'book_details.html', context)

def wish_list(request, user):
	"""Adds the book to the user's wish list.

	Parameters:
	request (request): Browser request for the view.

	"""

	u = User.objects.get(username=user)
	wished_books = u.whishes.all()

	page = request.GET.get('page', 1)
	paginator = Paginator(wished_books, 6) # Show 6 books per page
	
	try:
		books_list = paginator.page(page)
	except PageNotAnInteger:
		books_list = paginator.page(1)
	except EmptyPage:
		books_list = paginator.page(paginator.num_pages)
	

	context = {
		'books': wished_books,
		'books_list': books_list
	}

	return render(request, 'wish_list.html', context)


def search(request):
	"""Filters books by category and/or date and/or name.

	Parameters:
	request (request): Browser request for the view.

	"""
	categories = get_random_categories()
	success = True
	books = []
	category = request.GET.get('c')
	date = request.GET.get('t')
	name = request.GET.get('n')

	if (category is None and date is None and name is None):
		return redirect('/')
	
	if(category is not None):
		books = BestSellers.objects.filter(list_name=category).values_list('books')

	if(date is not None):
		books = BestSellers.objects.filter(day=date).values_list('books')

	if(name != None):
		books = Book.objects.filter(title__icontains=name)

	books = Book.objects.filter(pk__in=books)

	if not books:
		success = False
		books = Book.objects.all()

	page = request.GET.get('page', 1)

	paginator = Paginator(books, 6) # Show 6 books per page
	try:
		bestsellers = paginator.page(page)
	except PageNotAnInteger:
		bestsellers = paginator.page(1)
	except EmptyPage:
		bestsellers = paginator.page(paginator.num_pages)

	context = {
		'categories': categories,
		'success': success,
		'bestsellers': bestsellers
	}

	return render(request, 'home.html', context)

def category(request, pk):
	"""Filters books by category.

	Parameters:
	request (request): Browser request for the view.

	pk (isbn): International Standard Book Number, 10 or 13 digits.

	"""
	category = BestSellersListName.objects.get(pk=pk)
	api_to_db.update_best_sellers_list(category)
	categories = get_random_categories()

	latest = BestSellers.objects.order_by('-day').first()
	if latest is None:
		return redirect('/')
	bestsellers = BestSellers.objects.filter(list_name=pk, day=latest.day).values_list('books')
	books = Book.objects.filter(pk__in=bestsellers)

	page = request.GET.get('page', 1)
	paginator = Paginator(books, 6) # Show 6 books per page
	
	try:
		bestsellers_list = paginator.page(page)
	except PageNotAnInteger:
		bestsellers_list = paginator.page(1)
	except EmptyPage:
		bestsellers_list = paginator.page(paginator.num_pages)
	
	context = {
		'category': category,
		'categories': categories,
		'bestsellers_list': bestsellers_list
	}
	return render(request, 'category.html', context)

def emailView(request):
	submitted = False
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			email_adress = form.cleaned_data['email_adress']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, email_adress, ['admin@example.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			submitted = True
			form = ContactForm()
	return render(request, "contact.html", {'form': form, 'submitted': submitted})

def successView(request):
	return HttpResponse('Success! Thank you for your message.')

def edit_account(request):
	if request.method == 'POST':
		form = UserForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/account/')
		else:
			return redirect('/account/edit')
	else:
		form = UserForm(instance=request.user)
		args = {'form': form}
		return render(request, 'edit_account.html', args)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/account/edit/')
		else:
			return redirect('/change-password/')
	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form': form}
		return render(request, 'change_password.html', args)

class CommentViewSet(viewsets.ModelViewSet):
	permission_classes = [permissions.IsOwnerOrReadOnlyComment|IsAdminUser]

	def get_serializer_class(self):
		if self.request.method == 'POST':
			return serializers.PostCommentSerializer
		return serializers.GetCommentSerializer

	def get_queryset(self):
		queryset = Comment.objects.all()
		book_pk = self.request.query_params.get('book', None)
		if book_pk is not None:
			book_set = Book.objects.all().filter(isbn=book_pk)
			if not book_set.exists():
				return Comment.objects.none()
			queryset = queryset.filter(based_on=book_set.first())
		return queryset

class WishViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]

	def get_serializer_class(self):
		if self.request.method == 'POST':
			return serializers.PostWishSerializer
		return serializers.GetWishSerializer

	def get_queryset(self):
		queryset = Book.objects.all()
		user = self.request.user
		queryset = queryset.filter(whised_by=user)
		return queryset
