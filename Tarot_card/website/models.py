from django.db import models

# Create your models here.

class contact_lead(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email_id = models.EmailField(max_length=50)
    msg = models.TextField(max_length=150)

    def __str__(self):
        return self.phone_number


