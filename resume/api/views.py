from django.http import Http404
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.contrib.auth.models import User
from resume.api.serializers import ExperienceSerializer, BioSerializer, ExperienceChangeSerializer
from resume.models import Experience, Bio

################# Exp ###################

class ExperienceAPIView(ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = (AllowAny,)
    model = Experience

class ExperienceListAPIView(ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = (AllowAny,)
    model = Experience

class ExperienceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceChangeSerializer
    permission_classes = (IsAuthenticated,)
    model = Experience
    lookup_url_kwarg = 'experience_id'

#############  BIO  ###############

class BioListAPIView(ListAPIView):
    queryset = Bio.objects.all()
    serializer_class = BioSerializer
    permission_classes = (AllowAny,)
    model = Bio


class BioUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Bio.objects.all()
    serializer_class = BioSerializer
    permission_classes = (IsAuthenticated,)
    model = Bio
    lookup_url_kwarg = 'owner_id'
