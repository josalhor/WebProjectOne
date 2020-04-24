from django.db import models
from django.contrib.auth import models as auth_models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

class User(auth_models.AbstractUser):
	is_active = models.BooleanField(default=True, verbose_name='User activated')
	# this class doesn't need __str__ because it is inherited

class Book(models.Model):
	isbn = models.CharField(primary_key = True, max_length = 13, help_text = "13 characters")
	price = models.DecimalField(max_digits = 5, decimal_places = 2, validators=[MinValueValidator(0)])
	title = models.CharField(max_length = 150) 
	author = models.CharField(max_length = 150) 
	bestsellers_date = models.DateField()
	publisher = models.CharField(max_length = 150) 
	summary = models.TextField(max_length = 500, help_text = "Write a brief summary of this book, without spoiling")
	whished_by = models.ManyToManyField('User', related_name='whishes')
	
	def __str__(self):
		return '%s - %s' % (self.isbn, self.title)


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
	date = models.DateTimeField(auto_now_add=True)
	made_by = models.ForeignKey('User', on_delete = models.CASCADE)
	based_on = models.ForeignKey('Book', on_delete = models.CASCADE)

	def __str__(self):
		return '%s - %s: %s' % (self.made_by, self.based_on , self.title)

class BestSellersListName(models.Model):
	name = models.CharField(max_length = 150, help_text = "Name of the list")
	display_name = models.CharField(max_length = 150, help_text = "Display name of the list")
	list_name_encoded = models.CharField(primary_key=True, max_length = 150, help_text = "Encoded name of the list")
	
	def __str__(self):
		return f'{self.display_name}'

class BestSellers(models.Model):
	class Meta:
		unique_together = (('day', 'list_name'),)
	best_sellers_id = models.AutoField(primary_key=True)
	day = models.DateField(help_text = "Enter a day to find out which the best seller books were") 
	list_name = models.ForeignKey('BestSellersListName', on_delete = models.PROTECT)
	books = models.ManyToManyField('Book', related_name='best_seller_on')

	def __str__(self):
		return '%s' % (self.day)
