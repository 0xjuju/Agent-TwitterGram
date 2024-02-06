# Generated by Django 5.0.1 on 2024-02-06 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LLMConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('config_list', models.TextField(default='')),
                ('timeout', models.IntegerField(default=600)),
                ('cache_seed', models.IntegerField(default=42)),
                ('temperature', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('agent_type', models.CharField(default='assistant', max_length=255)),
                ('_code_execution_config', models.BooleanField(default=True)),
                ('system_message', models.CharField(default='', max_length=255)),
                ('llm_config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agents.llmconfig')),
            ],
        ),
    ]