import uuid
from django.db import models

# Create your models here.

class AccountCredentials(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    initial_url = models.CharField(blank=True, max_length=64)
    email = models.CharField(blank=True, max_length=64)
    API_key = models.CharField(blank=True,max_length=128)

