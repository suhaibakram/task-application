# Generated by Django 3.0.7 on 2020-06-17 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]