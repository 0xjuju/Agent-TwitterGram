# Generated by Django 5.0.1 on 2024-02-08 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0010_agent_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='llmconfig',
            name='use_docker',
            field=models.BooleanField(default=False),
        ),
    ]