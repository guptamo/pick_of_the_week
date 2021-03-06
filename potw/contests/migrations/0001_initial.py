# Generated by Django 3.0.7 on 2020-07-05 04:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=280)),
                ('pick_deadline', models.DateTimeField()),
                ('vote_deadline', models.DateTimeField()),
                ('spotify_playlist', models.SlugField()),
                ('youtube_playlist', models.SlugField()),
                ('admin_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
