# Generated by Django 4.1 on 2022-08-22 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0006_alter_note_options_alter_note_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'get_latest_by': ['-date']},
        ),
    ]
