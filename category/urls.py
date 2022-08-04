from django.urls import path
from category import views
urlpatterns = [
    path("vacancy/", views.VacancyListView.as_view())
]
