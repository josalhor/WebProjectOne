from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreationForm, ContactForm
from .models import Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
	page = request.GET.get('page', 1)

	paginator = Paginator(books, 6) # Show 6 books per page
	try:
		bestsellers = paginator.page(page)
	except PageNotAnInteger:
		bestsellers = paginator.page(1)
	except EmptyPage:
		bestsellers = paginator.page(paginator.num_pages)
	
	context = {
		'bestsellers': bestsellers
	}

	return render(request, 'home.html', context)


def book_details(request, pk):
	book = Book.objects.get(pk=pk)

	context = {
		'book': book
	}

	return render(request, 'book_details.html', context)
	# return render(request, 'home.html', context) ?

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