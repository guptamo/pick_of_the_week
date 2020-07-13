from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from .models import Contest, Pick
from .serializers import ContestSerializer, PickSerializer

class CreateContest(CreateAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer

class GetContest(RetrieveAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer

class CreatePick(CreateAPIView):
    queryset = Pick.objects.all()
    serializer_class = PickSerializer
