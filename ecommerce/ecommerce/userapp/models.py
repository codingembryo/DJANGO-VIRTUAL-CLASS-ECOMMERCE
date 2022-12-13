from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class Profile(models.Model):
    countries = [
        ("Nigeria", "Nigeria"),
        ("Ghana", "Ghana"),
        ("United Kingdom", "UK"),
        ("USA", "USA"),
    ]


    states = [

        ("Abia", "Abia"),
        ("Abia", "Abia"),
        ("Abia", "Abia"),
        ("Abia", "Abia"),
        ("Abia", "Abia"),
        ("Abia", "Abia"),
        ("Abia", "Abia"),
    ]

    position = [

        ("MD", "MD"),
        ("CEO", "CEO"),
        ("HOD", "HOD"),
        ("Accountant", "Accountant"),
        ("Secretary", "Secretary"),
        ("Admin", "Admin"),
        ("Clerical officer", "Clerical officer"),
        ("Technician", "Technician"),
        ("Sales officer", "Sales officer"),
        ("Marketing", "Marketing"),
        ("HR", "HR"),
    ]

    ma_status = [

        ("Single", "Single"),
        ("Married", "Married"),
        ("Divorce", "Divorce"),
        ("Complicate", "Complicate"),
    ]


    dept = [
        ("Marketing", "Marketing"),
        ("Sales", "Sales"),
        ("Admin", "Admin"),
        ("Production", "Production"),
        ("Accounting", "Accounting"),
        ("Electrical", "Electrical"),
    ]

    staff_status = [

        ("Active", "Active"),
        ("Suspended", "Suspended"),
        ("On Leave", "On Leave"),
        ("Retired", "Retired"),
        ("Resigned", "Resigned"),
    ]

    profile_id = models.AutoField(primary_key=True)

    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    address = models.CharField(unique=False, max_length=100, null=True)
    phone = models.CharField(unique=True, max_length=11, null=True)
    date_of_birth = models.CharField(unique=False, max_length=11, null=True)
    gender = models.CharField(unique=False, max_length=11, null=True)
    nationality = models.CharField(choices=countries, unique=False, max_length=50, null=True)
    state = models.CharField(choices=states, unique=False, max_length=50, null=True)
    means_of_identity = models.ImageField(upload_to='identityImage/', unique=False, null=True)
    particulars = models.FileField(upload_to='particularsImage//', unique=False, null=True)
    profile_passport = models.FileField(upload_to='staffImage/', unique=False, null=True)
    position = models.FileField(choices=position, unique=False, max_length=50, null=True)
    department = models.CharField(choices=dept, unique=False, max_length=50, null=True)
    marital_status = models.CharField(choices=ma_status, unique=False, max_length=20, null=True)
    staff = models.BooleanField(default=False, unique=False)
    next_of_kin = models.CharField(unique=False, max_length=20, null=True)
    status = models.CharField(choices=staff_status, unique=False, max_length=50, null=True, default="Active")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()



    