# Generated by Django 4.1.7 on 2023-03-13 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.habit'),
        ),
    ]
