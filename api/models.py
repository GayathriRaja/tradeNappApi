from django.db import models





# Create your models here.


class NewUser(models.Model):
    auto_increment_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,unique=True)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.fname