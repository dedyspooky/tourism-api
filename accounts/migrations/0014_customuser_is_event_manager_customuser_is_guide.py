# Generated by Django 5.0.6 on 2024-06-25 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_remove_customuser_is_event_manager_and_more'),
    ]

    operations = [
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