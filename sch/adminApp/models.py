from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class fees_table(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True)
    Full_tuition_fee = models.CharField(max_length=250, unique=False, null=True)
    part_tuition_fee = models.CharField(max_length=250, unique=False, null=True)
    late_reg_fee = models.CharField(max_length=250, unique=False, null=True)
    late_reg_approval = models.BooleanField(default=False, unique=False)
    admission_form_fee = models.CharField(max_length=250, unique=False, null=True)
    acceptance_fee = models.CharField(max_length=250, unique=False, null=True)
    last_updated = models.CharField(max_length=250, unique=False, null=True)
    date_added = models.DateTimeField(auto_now_add=True)



