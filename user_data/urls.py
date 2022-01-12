from django.urls import path
from . import views

urlpatterns = [
    path('create-candidate/', views.CandidateListCreate.as_view() ),
]