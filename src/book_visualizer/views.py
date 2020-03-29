from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreationForm, ContactForm
from .models import Book, BestSellersListName, BestSellers, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError


class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'sign_up.html'

# We are using reverse_lazy because for all generic class-based views the urls
# are not loaded when the file is imported, so we have to use the lazy form of
# reverse to load them later when they are available.

def bestsellers_list(request):
	books = Book.objects.all()
	categories = BestSellersListName.objects.all()
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
	book = Book.objects.get(pk=pk)
	comments = Comment.objects.all().filter(based_on = book)

	context = {
		'book': book,
		'comments': comments,
	}

	return render(request, 'book_details.html', context)

def search(request):
	categories = BestSellersListName.objects.all()
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
	category = BestSellersListName.objects.get(pk=pk)
	categories = BestSellersListName.objects.all()

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