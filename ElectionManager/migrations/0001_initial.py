# Generated by Django 2.1.7 on 2019-03-26 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Election_db',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(blank=True, max_length=30)),
                ('Start_Time', models.DateField(blank=True, null=True)),
                ('End_Time', models.DateField(blank=True, null=True)),
                ('List_Of_Choices', models.CharField(blank=True, max_length=500)),
                ('Number_Of_Votes', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
