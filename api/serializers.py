from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Expert


class ExpertSerializer(serializers.ModelSerializer):
	first_name = serializers.CharField(source='user.first_name', read_only=True)

	class Meta:
		model = Expert
		fields = ('first_name', 'title', 'rate', 'rating', 'description')

