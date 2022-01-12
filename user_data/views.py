from .models import Candidate
from .serializers import CandidateSerializer
from rest_framework import generics, serializers

# Create your views here.
class CandidateListCreate(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer