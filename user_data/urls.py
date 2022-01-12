from django.urls import path
from . import views

urlpatterns = [
    path('create-candidate/', views.CandidateListCreate.as_view() ),
    path('create-score/', views.ScoreListCreate.as_view() ),
    path('get-candidate/<slug:candidate_ref>', views.GetScoreListByCandidate.as_view()),
]