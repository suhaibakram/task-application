# Generated by Django 3.0.7 on 2020-06-17 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habitica', '0002_auto_20200617_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='taskcreator',
            new_name='userr',
        ),
    ]
