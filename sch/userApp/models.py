from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    gender_option = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    marital_status_option = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorce' , 'Divorce'),
        ('Complicated', 'Complicated'),
    ]

    next_of_kin_relationship_option = [
        ('Mother' , 'Mother'),
        ('Father' , 'Father'),
        ('Brother' , 'Brother'),
        ('Sister' , 'Sister'),
        ('Gaurdian' , 'Gaurdian'),
        ('Others' , 'Others'),
    ]

    approval_options = [
        ('-------', '-------'),
        ('Unapproved', 'Unapproved'),
        ('Approved', 'Approved'),
    ]



    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    other_name = models.CharField(unique=False, max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True, unique=False)
    phone_no = models.CharField(max_length=11, null=True, blank=True, unique=True)
    # email = models.EmailField(max_length=30, null=True, blank=True, unique=True)
    # matric_no = models.CharField(max_length=30, null=True, blank=True, unique=True)
    # level = models.CharField(max_length=30, null=True, blank=True, unique=False)
    # department = models.CharField(max_length=30, null=True, blank=True, unique=False)
    nin = models.CharField(max_length=11, null=True, blank=True, unique=True)
    d_o_b = models.DateField(unique=False, max_length=11, null=True)
    gender = models.CharField(choices=gender_option, unique=False, max_length=11, null=True)
    nationality = models.CharField(unique=False, max_length=50, null=True)
    state = models.CharField(unique=False, max_length=50, null=True)
    means_of_identity = models.ImageField(upload_to='identityImage/', unique=False, null=True)
    means_of_identity_approval = models.CharField(choices=approval_options, unique=False, max_length=10, null=True, default='Unapproved')
    particulars = models.FileField(upload_to='particularsImage/', unique=False, null=True)
    particulars_approval = models.CharField(choices=approval_options, unique=False, max_length=10, null=True, default='Unapproved')
    profile_passport = models.ImageField(upload_to='profileImage/', unique=False, null=True)
    marital_status = models.CharField(choices=marital_status_option, unique=False, max_length=20, null=True)
    staff = models.BooleanField(default=False, unique=False)
    next_of_kin = models.CharField(unique=False, max_length=30, null=True)
    next_of_kin_phone_no = models.CharField(max_length=11, null=True, blank=True, unique=True)
    next_of_kin_relationship = models.CharField(choices=next_of_kin_relationship_option, null=True, unique=False, max_length=15)
    category = models.CharField(max_length=20, null=True, blank=True, unique=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class users_status(models.Model):
    status_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student = models.BooleanField(default=False, unique=False)
    staff = models.BooleanField(default=False, unique=False)
    aspirant = models.BooleanField(default=False, unique=False)

@receiver(post_save, sender=User)
def create_user_status(sender, instance, created, **kwargs):
    if created:
        users_status.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_status(sender, instance, **kwargs):
    instance.users_status.save()