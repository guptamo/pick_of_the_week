from django.urls import path
from .views import CreateContest, GetContest, CreatePick

urlpatterns = [
    path('', CreateContest.as_view()),
    path('<int:pk>/', GetContest.as_view()),
    path('<int:pk>/pick/', CreatePick.as_view()),
]
