# Generated by Django 3.0.6 on 2020-05-05 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_visualizer', '0004_remove_book_price'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('made_by', 'based_on')},
        ),
    ]
