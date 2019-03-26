from django.db import models

# Create your models here.

class Election_db(models.Model):
 id = models.AutoField(primary_key=True)
 Title=models.CharField(max_length=30,null=False,blank=True)
 Start_Time=models.DateField(null=True,blank=True)
 End_Time=models.DateField(null=True,blank=True)
 List_Of_Choices=models.CharField(max_length=500,null=False,blank=True)
 Number_Of_Votes=models.IntegerField(null=True,blank=True)

 def __str__(self):
  return str(self.Title)