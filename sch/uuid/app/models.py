from django.db import models
from django.contrib.auth.models import User
import uuid

class Item(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, unique=False, null=True)