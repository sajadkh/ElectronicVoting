# Generated by Django 2.1.7 on 2019-04-16 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ElectionManager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listofchoices',
            old_name='Election',
            new_name='Election_ref',
        ),
        migrations.RenameField(
            model_name='listofchoices',
            old_name='Choice',
            new_name='Title',
        ),
    ]