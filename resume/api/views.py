from django.http import Http404
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.contrib.auth.models import User
from resume.api.serializers import ExperienceSerializer, BioSerializer
from resume.models import Experience, Bio

################# Exp ###################

class ExperienceAPIView(ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    model = Experience

class ExperienceListAPIView(ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    model = Experience

class ExperienceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    model = Experience
    lookup_url_kwarg = 'experience_id'

#############  BIO  ###############

class BioListAPIView(ListCreateAPIView):
    queryset = Bio.objects.all()
    serializer_class = BioSerializer
    model = Bio


class BioUpdateAPIView(UpdateAPIView):
    queryset = Bio.objects.all()
    serializer_class = BioSerializer
    model = Bio
    lookup_url_kwarg = 'owner_id'
