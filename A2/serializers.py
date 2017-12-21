from django.contrib.auth.models import User, Group
from .models import Task
from rest_framework import serializers
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('owner', 'taskname', 'text', 'due_date', 'important')
		"""
		owner = serializers.CharField(read_only=True)
		taskname = serializers.CharField(max_length=200)
		text = serializers.CharField(required=False)
		due_date = serializers.DateField(default=timezone.now)
		important = serializers.BooleanField(required=False)

		def create(self, validated_data):
		"""
		#Create and return a new `Task` instance, given the validated data.
		"""
		return Task.objects.create(**validated_data)

		def update(self, instance, validated_data):
		"""
		#Update and return an existing `Task` instance, given the validated data.
		"""
		instance.taskname = validated_data.get('taskname', instance.taskname)
		instance.text = validated_data.get('text', instance.text)
		instance.due_date = validated_data.get('due_date', instance.due_date)
		instance.important = validated_data.get('important', instance.important)
		instance.save()
		return instance
		"""

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')