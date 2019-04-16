from django.db import models


# Create your models here.

class Election(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=30)
    Start_Time = models.DateField()
    End_Time = models.DateField()
    Number_Of_Votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.Title)


class ListOfChoices(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=1000)
    Election_ref = models.ForeignKey(Election, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Title)