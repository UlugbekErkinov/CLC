from django.db import models
from common.models import User
from helpers.models import BaseModel

class Category(BaseModel):
    title = models.CharField(max_length=255, blank=True, default=False)

    def __str__(self):
        return self.title

class Company(BaseModel):
    title = models.CharField(max_length=255, blank=True, default=False)

    def __str__(self):
        return self.title

class Employer(BaseModel):
    name = models.CharField(max_length=255, blank=True, default=False)

    def __str__(self):
        return self.name


class Vacancy(BaseModel):
    title = models.CharField(max_length=255, blank=True, default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company")
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name="employer")
    salary = models.PositiveIntegerField(default=False)


    def __str__(self):
        return self.title
