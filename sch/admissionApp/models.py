from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class aspirants_profile(models.Model):
    next_of_kin_relationship_option = [
        ("Brother", "Brother"),
        ("Father", "Father"),
        ("Mother", "Mother"),
        ("Sister", "Sister"),
        ("Other", "Other"),
    ]
    course_options = [
        ("Digital Marketing", "Digital Marketing"),
        ("Business World", "Business World"),
        ("Media Technology", "Media Technology"),
        ("Communications", "Communications"),
        ("Business Ethics", "Business Ethics"),
    ]
    marital_status_options = [
         ("Single", "Single"),
         ("Married", "Married"),
         ("Others", "Others"),
     ]
    sponsorhip_options = [
         ("Parents", "Parents"),
         ("Guardian", "Guardian"),
         ("Others", "Others"),
     ]
    aspirant_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=False, null=True)
    sponsorhip = models.CharField(choices=sponsorhip_options, unique=False, max_length=50, null=True, blank=True)
    country = models.CharField(unique=False, max_length=50, null=True, blank=True)
    state = models.CharField(unique=False, max_length=50, null=True, blank=True)
    course = models.CharField(choices=course_options, unique=False, max_length=50, null=True)
    next_of_kin_email = models.CharField(unique=False, max_length=30, null=True)
    next_of_kin_address = models.CharField(unique=False, max_length=50, null=True)
    passport = models.FileField(upload_to='passportImage/', unique=False, null=True)
    o_levels = models.FileField(upload_to='o_levelImage/', unique=False, null=True)
    utme = models.FileField(upload_to='utmeImage/', unique=False, null=True)
    national_identity = models.FileField(upload_to='national_IdentityImage/', unique=False, null=True)
    registration_status = models.BooleanField(default=False)
    created_time = models.DateField(auto_now_add=True, unique=False, null=True)


class admission_approval(models.Model):
    admission_id = models.AutoField(primary_key=True)
    aspirant = models.OneToOneField(aspirants_profile, on_delete=models.CASCADE, null=True)
    officer_incharge = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False)
    acceptance_fee = models.BooleanField(default=False)
    approved_date = models.DateField(auto_now_add=True, unique=False, null=True)