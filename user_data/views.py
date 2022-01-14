from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from .models import Candidate, Score
from .serializers import CandidateSerializer, ScoreSerializer
from rest_framework import generics
from user_data import serializers
from django.db import connection

#
class CandidateListCreate(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class ScoreListCreate(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer



#Code commented out as 'get score by candidate' endpoint not functioning correctly.
#Using method prefetch_related did not work as expected
#The SQL query below works correctly when querying sqlite3 directly, but is not functioning correctly when passed via django

# class GetScoreListByCandidate(generics.ListAPIView):
#     serializer_class = CandidateSerializer

#     def get_queryset(self):
#         candidate_ref = self.kwargs['candidate_ref']

#         return Candidate.objects.raw(
#             'SELECT candidate_ref, name, GROUP_CONCAT(user_data_score.score) FROM user_data_candidate JOIN user_data_score ON ("user_data_candidate"."candidate_ref" = "user_data_score"."candidate_ref_id") WHERE candidate.candidate_ref = %s GROUP BY user_data_candidate.candidate_ref ;', [candidate_ref]
#         )