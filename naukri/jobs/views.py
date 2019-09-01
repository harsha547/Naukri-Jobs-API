from django.shortcuts import render
from .models import Job

from rest_framework import generics
from .serializers import JobSerializer

class ListJob(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class DetailJob(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer