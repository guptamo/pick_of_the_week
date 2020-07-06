from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from .models import Contest
from .serializers import ContestSerializer

class CreateContest(CreateAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer

class GetContest(RetrieveAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer