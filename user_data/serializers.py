from rest_framework import serializers
from .models import Candidate, Score

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('candidate_ref', 'name')


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('score_ref', 'candidate_ref', 'score')