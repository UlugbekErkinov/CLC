from django.shortcuts import render
from .models import Category, Employer, Company, Vacancy
from rest_framework import generics

from django.db import models

from common.models import User
from category import serializer
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.vary import vary_on_headers
# Create your views here.


class VacancyListView(generics.ListAPIView):
    queryset = Vacancy.objects.filter('company','vacancy', 'employer').count()
    serializer_class = serializer.VacancySerializer

    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_headers("Authorization",))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    

