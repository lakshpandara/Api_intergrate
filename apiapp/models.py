from django.db import models

class APIData(models.Model):
	Country = models.CharField(max_length=50)
	Slug = models.CharField(max_length=50)
