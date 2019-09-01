from django.urls import path
from .views import ListJob, DetailJob

urlpatterns = [
    path('<int:pk>/', DetailJob.as_view()),
    path('', ListJob.as_view())
]