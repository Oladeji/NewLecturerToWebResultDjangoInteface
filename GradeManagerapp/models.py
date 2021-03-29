from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils import timezone
#import datetime

class Lecturer(User):
    

    class Meta:
        proxy = True


class AvailableSemester(models.Model):
     myCampId = models.CharField(max_length=20)
     myProgId = models.CharField(max_length=10)
     myAsetId = models.CharField(max_length=10)
     myAsessionId = models.CharField(max_length=10)
     mySemesterId = models.CharField(max_length=1)
     myTheprogType = models.CharField(max_length=10)
     myRemark = models.CharField(max_length=30)



class UploadedScores(models.Model):
     #courseGuId  = models.UUIDField( default=uuid.uuid4, editable=True)
     title = models.CharField(default= 'Mydefault title',max_length=100)
     upload_date = models.DateTimeField('upload date', default= timezone.now())
     scoresheetfile = models.FileField(upload_to='ScoresFolder/%Y/%m/%d')

     def __str__(self):
          return self.title

