
from django.contrib.auth.models import User
from resume.models import Experience, Bio
from rest_framework import serializers, pagination, generics

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['title', 'start','end', 'content',]

class ExperienceChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'title', 'start','end', 'content','owner']


class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields = ['name', 'email','about']

