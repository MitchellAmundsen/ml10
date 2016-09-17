from django.db import models

class Book(models.Model):
	title = models.CharField(max_length = 100)
	date = models.DateField()
	publisher = models.CharField(max_length = 100)
	summary = models.CharField(max_length = 1000)
	price = models.DecimalField(decimal_places = 2, max_digits = 5)
	link = models.URLField()
	img = models.URLField()

class Author(models.Model):
	books = models.ManyToManyField(Book)
	fname = models.CharField(max_length = 20)
	lname = models.CharField(max_length = 30)


# Create your models here.
