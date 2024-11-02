from django.db import models
from django.contrib.auth.models import User
from admissionApp.models import aspirants_profile
from adminApp.models import fees_table

# Create your models here.

class invoice_table(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, unique=False)
    amount = models.CharField(max_length=50, unique=False)
    transaction_type = models.CharField(max_length=50, unique=False, null=True)
    category = models.CharField(max_length=50, unique=False, null=True)
    status = models.CharField(max_length=50, unique=False, default='unsuccessful')
    completed = models.BooleanField(default=False, unique=False)
    date = models.DateTimeField(auto_now=True, unique=False)

class admission_invoice_table(models.Model):
    adInv_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True)
    invoice = models.ForeignKey(invoice_table, on_delete=models.CASCADE, unique=False)
    form_fee = models.CharField(max_length=50, unique=False)
    paid = models.BooleanField(default=False, unique=False)
    date_created = models.DateTimeField(auto_now=True, unique=False)

class acceptance_invoice_table(models.Model):
    accInv_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True)
    invoice = models.ForeignKey(invoice_table, on_delete=models.CASCADE, unique=False)
    acceptance_fee = models.CharField(max_length=50, unique=False)
    paid = models.BooleanField(default=False, unique=False)
    date_created = models.DateTimeField(auto_now=True, unique=False)


class tuition_invoice_table(models.Model):
    tuitInv_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True)
    invoice = models.ForeignKey(invoice_table, on_delete=models.CASCADE, unique=False, null=True)
    tuition_fee = models.CharField(max_length=50, unique=False)
    paid = models.BooleanField(default=False, unique=False)
    date_created = models.DateTimeField(auto_now=True, unique=False)

class lateReg_invoice_table(models.Model):
    regInv_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True)
    tuition = models.ForeignKey(tuition_invoice_table, on_delete=models.CASCADE, unique=False, null=True)
    fee = models.CharField(max_length=20, unique=False)
    paid = models.BooleanField(default=False, unique=False)
    date_created = models.DateTimeField(auto_now=True, unique=False)
