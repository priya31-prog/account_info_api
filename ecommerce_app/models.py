from django.db import models

# Create your models here.


# using functions
class AccountInfo(models.Model):
    userid = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=200, unique=True)
    phoneNumber = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    profileImage = models.CharField(
        max_length=400,
        null=True,
        blank=True,
    )
    email = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "accountinfo"


# using class methods in view


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    streetName = models.CharField(max_length=200)
    addressLine1 = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    accountInfo_userid = models.CharField(max_length=50)

    class Meta:
        db_table = "address"
