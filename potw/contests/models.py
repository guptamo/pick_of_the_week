from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class League(models.Model):
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=280)

    def __str__(self):
        return self.name


class Contest(models.Model):
    league_id = models.ForeignKey(League, null=True, on_delete=models.SET_NULL)
    theme = models.CharField(max_length=280)
    pick_deadline = models.DateTimeField(default=datetime.utcnow() + timedelta(days=5))
    vote_deadline = models.DateTimeField(
        default=datetime.utcnow() + timedelta(days=7))
    admin_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    spotify_playlist = models.URLField(null=True)
    youtube_playlist = models.URLField(null=True)

    def get_status(self):
        if timezone.now() < self.pick_deadline:
            return 'picking'
        elif self.pick_deadline < timezone.now() < self.vote_deadline:
            return 'voting'
        else:
            return 'closed'

    def __str__(self):
        return f'Contest {self.id}: {self.theme}'


class Pick(models.Model):
    contest_id = models.ForeignKey(Contest, on_delete=models.SET_NULL, null=True)
    picked_by = models.CharField(max_length=280)
    artist = models.CharField(max_length=280)
    song = models.CharField(max_length=280)
    spotify_track = models.URLField(null=True)
    youtube_video = models.URLField(null=True)

    def __str__(self):
        return f'{self.song} picked by {self.picked_by}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['contest_id', 'picked_by'], name='unique_by_contest_and_picked_by')
        ]
