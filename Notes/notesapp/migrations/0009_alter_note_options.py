# Generated by Django 4.1 on 2022-08-22 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0008_alter_note_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['date']},
        ),
    ]