from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    bio = models.TextField(null=True, blank=True)

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        if self.age is not None and self.age < 0:
            raise ValidationError("Age must be a positive number.")

