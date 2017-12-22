from django.contrib.auth.models import User, Group
from .models import Task
from rest_framework import serializers
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('owner', 'pk', 'taskname', 'text', 'due_date', 'important')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')