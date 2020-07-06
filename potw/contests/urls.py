from django.urls import path
from .views import CreateContest, GetContest

urlpatterns = [
    path('', CreateContest.as_view()),
    path('<int:pk>/', GetContest.as_view()),
]
