# Generated by Django 4.1 on 2022-08-22 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0004_alter_note_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'get_latest_by': ['-date']},
        ),
    ]
