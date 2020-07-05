from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .models import Contest
from .serializers import ContestSerializer

class CreateContest(CreateAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
