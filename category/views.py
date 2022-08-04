from django.shortcuts import render
from .models import Category, Employer, Company, Vacancy
from rest_framework import generics
from rest_framework.response import Response

from django.db import models

from common.models import User
from category import serializer
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.vary import vary_on_headers

from .serializer import VacancySerializer, CategorySerializer, EmployerSerializer, CompanySerializer

# Create your views here.


class VacancyListView(generics.ListAPIView):
    
    # @method_decorator(cache_page(60*60*2))
    # @method_decorator(vary_on_headers("Authorization",))
    def get(self, *args, **kwargs):
        V = Vacancy.objects.count()
        E = Employer.objects.count()
        C = Company.objects.count()
        return Response({'Number of Vacancies': V, 'Number of Employers': E, 'Number of Companies': C})


    

