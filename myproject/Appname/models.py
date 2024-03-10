from django.db import models

# Create your models here.


class LoginTable(models.Model):
    id = models.AutoField(primary_key=True)
    username= models.CharField(max_length=30,blank=False,unique=True)
    # blank = false means name cannot be blank.
    #unique = true means name should be unique.
    password=models.CharField(max_length=10,blank=False,unique=False)
    class Meta:
        db_table="Login_Table"
