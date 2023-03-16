# Generated by Django 4.1.7 on 2023-03-16 18:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_habit_observers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='observers',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
