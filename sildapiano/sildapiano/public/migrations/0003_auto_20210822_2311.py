# Generated by Django 3.2.6 on 2021-08-22 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_lessonplans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='age_above_18',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='renting',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
