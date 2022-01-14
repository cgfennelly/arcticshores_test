"""Unit testing in progress. Not complete."""

# import json
# from rest_framework import status
# from django.test import TestCase, Client
# from django.urls import reverse

# from user_data.views import CandidateListCreate
# from .models import Candidate, Score
# from .serializers import CandidateSerializer, ScoreSerializer


# # initialize the APIClient app
# client = Client()

# class GetAllCandidatesTest(TestCase):
#     """ Test module for GET all Candidate API """

#     def setUp(self):
#         Candidate.objects.create(
#             candidate_ref='abcd1234', name='Casper')
#         Candidate.objects.create(
#             candidate_ref='5678efgh', name='Lazzo')

#     def test_get_all_candidates(self):
#         # get API response
#         response = client.get(reverse(CandidateListCreate))
#         # get data from db
#         candidates = Candidate.objects.all()
#         serializer = CandidateSerializer(candidates, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)