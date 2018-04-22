from django.db import models
from django.contrib.auth.models import User


class Expert(models.Model):
	user  = models.OneToOneField(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	rate = models.IntegerField(default=0)
	rating = models.IntegerField(default=0)
	description = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return u"%s" % self.user.email
