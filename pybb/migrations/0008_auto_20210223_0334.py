# Generated by Django 3.1.5 on 2021-02-23 03:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybb', '0007_auto_20170111_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='moderators',
            field=models.ManyToManyField(blank=True, related_name='moderators_forum', to=settings.AUTH_USER_MODEL, verbose_name='Moderators'),
        ),
    ]
