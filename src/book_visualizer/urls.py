from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from . import forms, views

urlpatterns = [
	path('login/', LoginView.as_view(authentication_form=forms.AuthenticationForm), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('sign_up/', views.SignUp.as_view(), name='sign-up'),
	path('account/', TemplateView.as_view(template_name='account.html'), name='account'),
	path('', include('django.contrib.auth.urls')),
	path('', views.bestsellers_list, name='home'),
		path('<int:pk>', views.book_details, name='book_details'), 
]
