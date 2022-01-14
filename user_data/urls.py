from django.urls import path
from . import views

urlpatterns = [
    path('create-candidate/', views.CandidateListCreate.as_view() ),
    path('create-score/', views.ScoreListCreate.as_view() ),
    #'get-candidate' route commented out as it is not functioning correctly
    # path('get-candidate/<slug:candidate_ref>', views.GetScoreListByCandidate.as_view()),
]