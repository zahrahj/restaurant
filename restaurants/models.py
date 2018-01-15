from django.db import models

# Create your m

class Restaurant(models.Model):
	logo = models.ImageField(null=True, blank=True)
	name = models.CharField(max_length=120)
	description = models.TextField(null=True)
	opening_time = models.TimeField(null=True)
	closing_time = models.TimeField(null=True)