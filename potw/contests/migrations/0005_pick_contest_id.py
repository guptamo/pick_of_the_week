# Generated by Django 3.0.7 on 2020-07-06 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0004_pick'),
    ]

    operations = [
        migrations.AddField(
            model_name='pick',
            name='contest_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contests.Contest'),
            preserve_default=False,
        ),
    ]
