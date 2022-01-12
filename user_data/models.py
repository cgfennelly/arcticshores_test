from django.db import models

# Create your models here.
class Candidate(models.Model):
    candidate_ref = models.CharField(primary_key=True, max_length=8)
    name = models.CharField