from django.db import models
from django.contrib.auth import models as auth_models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

class User(auth_models.AbstractUser):
	# Changing the default value to False and the name shown 
	# in the admin interface to 'User activated'.
	is_active = models.BooleanField(default=False, verbose_name='User activated')


class Book(models.Model):
	isbn = models.CharField(primary_key = True, max_length = 13, help_text = "13 characters")
	price = models.DecimalField(max_digits = 5, decimal_places = 2, validators=[MinValueValidator(0)])
	image = models.ImageField(default="default.png", null = True)
	title = models.CharField(max_length = 150) 
	author = models.CharField(max_length = 150) 
	publication_date = models.DateField() 
	publisher = models.CharField(max_length = 150) 
	summary = models.TextField(max_length = 500, help_text = "Write a brief summary of this book, without spoiling")
	whished_by = models.ManyToManyField('User', related_name='whishes')

STARS = [
	("1", "1"),
	("2", "2"),
	("3", "3"),
	("4", "4"),
	("5", "5")
]
class Comment(models.Model):
	title = models.CharField(max_length = 150, help_text = "Write a useful title for your comment") 
	body = models.TextField(max_length = 500, help_text = "Write a comment to a book")
	stars = models.CharField(max_length=1, choices=STARS)
	made_by = models.ForeignKey('User', on_delete = models.CASCADE)
	based_on = models.ForeignKey('Book', on_delete = models.CASCADE)
