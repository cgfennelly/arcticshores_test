from .models import Candidate, Score
from .serializers import CandidateSerializer, ScoreSerializer
from rest_framework import generics

from user_data import serializers

# Create your views here.
class CandidateListCreate(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class ScoreListCreate(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class GetScoreListByCandidate(generics.ListAPIView):
    serializer_class = ScoreSerializer

    def get_queryset(self):
        candidate_ref = self.kwargs['candidate_ref']
        return Score.objects.filter(candidate_ref=candidate_ref)
