from django.db import models

# Create your models here.


class jobs(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.TextField(max_length=2000)
