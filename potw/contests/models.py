from django.db import models
from django.contrib.auth.models import User
import datetime

class Contest(models.Model):
    theme = models.CharField(max_length=280)
    pick_deadline = models.DateTimeField(null=True)
    vote_deadline = models.DateTimeField(null=True)
    admin_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    spotify_playlist = models.URLField(null=True)
    youtube_playlist = models.URLField(null=True)

    def get_status(self):
        if datetime.utcnow() < pick_deadline:
            return 'picking'
        elif pick_deadline < datetime.utcnow() < vote_deadline:
            return 'voting'
        else:
            return 'closed'

    def __str__(self):
        return f'Contest {self.id}: {self.theme}'

