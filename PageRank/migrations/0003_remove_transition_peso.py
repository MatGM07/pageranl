# Generated by Django 5.0.4 on 2024-04-19 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PageRank', '0002_transition_delete_userlinktransition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transition',
            name='peso',
        ),
    ]
