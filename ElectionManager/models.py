from django.db import models


# Create your models here.

class Election(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=30)
    Start_Time = models.DateField()
    End_Time = models.DateField()
    # List_Of_Choices = models.CharField(max_length=1000)
    Number_Of_Votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.Title)


class ListOfChoices(models.Model):
    id = models.AutoField(primary_key=True)
    Choices = models.CharField(max_length=1000)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
