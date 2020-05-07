from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from rest_framework import routers
from . import forms, views
from .views import emailView, successView

router = routers.DefaultRouter()
router.register('comments', views.CommentViewSet, 'Comments')
router.register('wishes', views.WishViewSet, 'Wishes')

urlpatterns = [
	path('login/', LoginView.as_view(authentication_form=forms.AuthenticationForm), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('sign_up/', views.SignUp.as_view(), name='sign-up'),
	path('account/<str:user>', views.wish_list, name='wish_list'),
	path('account/', TemplateView.as_view(template_name='account.html'), name='account'),
	path('contact/', emailView, name='contact'),
	path('search', views.search, name='search'),
	path('account/edit/', views.edit_account, name='edit_account'),
	path('change-password/', views.change_password, name='change_password'),
	path('', include('django.contrib.auth.urls')),
	path('', views.bestsellers_list, name='home'),
		path('book/<str:pk>', views.book_details, name='book_details'), 
		path('category/<str:pk>', views.category, name='category'),
	path('api/', include(router.urls))
]