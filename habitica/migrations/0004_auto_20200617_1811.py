# Generated by Django 3.0.7 on 2020-06-17 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habitica', '0003_auto_20200617_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='userr',
            new_name='user',
        ),
    ]