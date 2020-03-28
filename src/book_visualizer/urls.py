from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from . import forms, views
from .views import emailView, successView

urlpatterns = [
	path('login/', LoginView.as_view(authentication_form=forms.AuthenticationForm), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('sign_up/', views.SignUp.as_view(), name='sign-up'),
	path('account/', TemplateView.as_view(template_name='account.html'), name='account'),
	path('contact/', emailView, name='contact'),
	path('search', views.search, name='search'),
	path('', include('django.contrib.auth.urls')),
	path('', views.bestsellers_list, name='home'),
		path('book/<str:pk>', views.book_details, name='book_details'), 
		path('category/<str:pk>', views.category, name='category')
]