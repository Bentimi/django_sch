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

    department_options = [
        ("Digital Marketing", "Digital Marketing"),
        ("Business World", "Business World"),
        ("Media Technology", "Media Technology"),
        ("Communications", "Communications"),
        ("Business Ethics", "Business Ethics"),
    ]

    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    other_name = models.CharField(unique=False, max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True, unique=False)
    phone_no = models.CharField(max_length=11, null=True, blank=True, unique=True)
    # email = models.EmailField(max_length=30, null=True, blank=True, unique=True)
    # matric_no = models.CharField(max_length=30, null=True, blank=True, unique=True)
    # level = models.CharField(max_length=30, null=True, blank=True, unique=False)
    department = models.CharField(choices=department_options, max_length=50, unique=False, null=True)
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
    next_of_kin_email = models.CharField(max_length=50, null=True, blank=True, unique=False)
    next_of_kin_address = models.CharField(max_length=250, null=True, blank=True, unique=False)
    next_of_kin_relationship = models.CharField(choices=next_of_kin_relationship_option, null=True, unique=False, max_length=15)
    status = models.CharField(max_length=20, null=True, blank=True, unique=True)

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


class student_table(models.Model):
    id = models.AutoField(primary_key=True)
    matric_number = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    year = models.CharField(max_length=20, unique=False, null=True)
    sequence = models.PositiveIntegerField(unique=True, editable=False, default=1)
    department = models.CharField(max_length=50, unique=False, null=True)
    status = models.CharField(max_length=15, unique=False, default='Active')
    date_added = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.matric_number:
            # Get the highest matric number so far and add 1
            last_student = student_table.objects.all().order_by('sequence').last()
            if last_student:
                self.sequence = last_student.sequence + 1
            else:
                self.sequence = 1  # start from 1 if it's the first student
        super().save(*args, **kwargs)


class staff_table(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    department = models.CharField(max_length=50, unique=False, null=True)
    status = models.CharField(max_length=15, unique=False, default='Active')
    updated_user = models.ForeignKey(users_status, on_delete=models.CASCADE, null=True)
    last_updated = models.CharField(max_length=50, unique=False, null=True)
    staff_id = models.CharField(max_length=20, unique=True, null=True)
    status = models.CharField(max_length=15, unique=False, default='Active')
    date_added = models.DateTimeField(auto_now=True)
