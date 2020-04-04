from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models, forms

class UserAdmin(BaseUserAdmin):
	# The forms to add and change user instances
	add_form = forms.UserCreationForm
	form = forms.UserChangeForm

    # The custom user model we are going to use
	model = models.User

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Book)
admin.site.register(models.Comment)
admin.site.register(models.BestSellers)
admin.site.register(models.BestSellersListName)