# Generated by Django 3.1.5 on 2021-02-27 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20210227_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='publications',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]
