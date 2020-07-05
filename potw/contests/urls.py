from django.urls import path
from .views import CreateContest

urlpatterns = [
    path('', CreateContest.as_view())
]
