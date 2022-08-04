from django.shortcuts import render
from .models import Category, Employer, Company, Vacancy
from rest_framework import generics

from django.db import models

from common.models import User
from category import serializer

# Create your views here.


class VacancyListView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = serializer.VacancySerializer

    def get_queryset(self):
        return

