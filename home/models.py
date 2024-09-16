from django.db import models

# Create your models here.

class Advertise(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company_name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100)
    advertise = models.CharField(max_length=255)  # Ensure the field is correctly named
    budget = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)


    def __str__(self) -> str:
        return self.company_name

    class Meta:
        ordering = ['company_name']

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    company=models.CharField(max_length=100)
    messages=models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.company
    
    class Meta:
        ordering = ['company']