from django.db import models
from django.contrib.auth.models import User


class Expert(models.Model):
	user  = models.OneToOneField(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	rate = models.IntegerField(default=0)
	rating = models.IntegerField(default=0)
	description = models.TextField()

	def __str__(self):
		return u"%s" % self.user.email
