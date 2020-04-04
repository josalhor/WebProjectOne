# Generated by Django 3.0.5 on 2020-04-03 20:03

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='User activated')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BestSellersListName',
            fields=[
                ('name', models.CharField(help_text='Name of the list', max_length=150)),
                ('display_name', models.CharField(help_text='Display name of the list', max_length=150)),
                ('list_name_encoded', models.CharField(help_text='Encoded name of the list', max_length=150, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(help_text='13 characters', max_length=13, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('image', models.URLField(blank=True, help_text='URL of the image', null=True)),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('publication_date', models.DateField()),
                ('publisher', models.CharField(max_length=150)),
                ('summary', models.TextField(help_text='Write a brief summary of this book, without spoiling', max_length=500)),
                ('whished_by', models.ManyToManyField(related_name='whishes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Write a useful title for your comment', max_length=150)),
                ('body', models.TextField(help_text='Write a comment to a book', max_length=500)),
                ('stars', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1)),
                ('based_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_visualizer.Book')),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BestSellers',
            fields=[
                ('best_sellers_id', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.DateField(help_text='Enter a day to find out which the best seller books were')),
                ('books', models.ManyToManyField(related_name='best_seller_on', to='book_visualizer.Book')),
                ('list_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book_visualizer.BestSellersListName')),
            ],
            options={
                'unique_together': {('day', 'list_name')},
            },
        ),
    ]
