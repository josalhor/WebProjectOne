from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreationForm
from .models import Book

class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'sign_up.html'

# We are using reverse_lazy because for all generic class-based views the urls
# are not loaded when the file is imported, so we have to use the lazy form of
# reverse to load them later when they are available.

def bestsellers_list(request):
	bestsellers = Book.objects.all()

	context = {
		'bestsellers': bestsellers
	}

	return render(request, 'home.html', context)