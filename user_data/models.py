from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Candidate(models.Model):
    candidate_ref = models.CharField(primary_key=True, max_length=8)
    name = models.TextField()


class Score(models.Model):
    candidate_ref = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    score = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
