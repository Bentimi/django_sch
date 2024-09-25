from django.db import models
# from django_countries.fields import CountryField

# Create your models here.

class aspirants_profile(models.Model):
    gender_options = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    next_of_kin_relationship_option = [
        ("Brother", "Brother"),
        ("Father", "Father"),
        ("Mother", "Mother"),
        ("Sister", "Sister"),
        ("Other", "Other"),
    ]
    aspirant_id = models.AutoField(primary_key=True)
    first_name  = models.CharField(unique=False, max_length=50)
    middle_name = models.CharField(unique=False, max_length=50)
    last_name = models.CharField(unique=False, max_length=50)
    username = models.CharField(unique=True, max_length=50, null=True, blank=True)
    gender = models.CharField(choices=gender_options, unique=False, max_length=10, null=True)
    d_o_b = models.DateField(unique=False, max_length=11, null=True,)
    phone_no = models.CharField(unique=True, max_length=15)
    email = models.EmailField(unique=True, max_length=50)
    address = models.CharField(unique=False, max_length=500, null=True, blank=True)
    country = models.CharField(unique=False, max_length=50, null=True, blank=True)
    state = models.CharField(unique=False, max_length=50, null=True, blank=True)
    next_of_kin = models.CharField(unique=False, max_length=20, null=True)
    next_of_kin_number = models.CharField(unique=False, max_length=15, null=True)
    next_of_kin_email = models.CharField(unique=False, max_length=30, null=True)
    next_of_kin_relationship = models.CharField(choices=next_of_kin_relationship_option, unique=False, max_length=15, null=True)
    passport = models.FileField(upload_to='passportImage/', unique=True, null=True)
    o_levels = models.FileField(upload_to='o_levelImage/', unique=True, null=True)
    utme = models.FileField(upload_to='utmeImage/', unique=True, null=True)
    password = models.CharField(max_length=80, unique=False, null=False, blank=False)


class admission_approval(models.Model):
    admission_id = models.AutoField(primary_key=True)
    aspirant = models.OneToOneField(aspirants_profile, on_delete=models.CASCADE)
    admitted = models.BooleanField(default=False)