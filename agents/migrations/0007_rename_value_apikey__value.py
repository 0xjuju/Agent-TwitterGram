# Generated by Django 5.0.1 on 2024-02-06 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0006_rename_name_apikey_model_name_remove_llmconfig_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apikey',
            old_name='value',
            new_name='_value',
        ),
    ]