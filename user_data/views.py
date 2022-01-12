from .models import Candidate, Score
from .serializers import CandidateSerializer, ScoreSerializer
from rest_framework import generics

# Create your views here.
class CandidateListCreate(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class ScoreListCreate(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer