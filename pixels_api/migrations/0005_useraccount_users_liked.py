# Generated by Django 3.2.6 on 2021-08-22 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixels_api', '0004_auto_20210821_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='users_liked',
            field=models.ManyToManyField(blank=True, to='pixels_api.UserAccount'),
        ),
    ]
