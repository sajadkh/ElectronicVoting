# Generated by Django 2.1.7 on 2019-03-29 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElectionManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election_db',
            name='End_Time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='election_db',
            name='List_Of_Choices',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='election_db',
            name='Number_Of_Votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='election_db',
            name='Start_Time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='election_db',
            name='Title',
            field=models.CharField(max_length=30),
        ),
    ]