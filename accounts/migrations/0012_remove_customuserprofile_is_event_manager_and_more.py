# Generated by Django 5.0.6 on 2024-06-25 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_guiderating_tour_delete_tour_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuserprofile',
            name='is_event_manager',
        ),
        migrations.RemoveField(
            model_name='customuserprofile',
            name='is_guide',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_event_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_guide',
            field=models.BooleanField(default=False),
        ),
    ]
