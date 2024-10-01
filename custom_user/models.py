import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class InterestCategory(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Interest(models.Model):
    name = models.CharField(max_length=80)
    category = models.ForeignKey(InterestCategory, on_delete=models.CASCADE, related_name="interests")

    def __str__(self):
        return self.name
    

class UserInterest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'interest')

    def __str__(self):
        return f'{self.user} - {self.interest}'
    
