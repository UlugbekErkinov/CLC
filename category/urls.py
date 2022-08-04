from django.urls import path
from category import views
urlpatterns = [
    path("category/", views.VacancyListView.as_view())
]
