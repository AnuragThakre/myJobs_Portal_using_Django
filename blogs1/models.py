from django.db import models

# Create your models here.


class blogs1(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        return self.body[0:101]

    def __str__(self):
        return self.title

    def pub_date_preety(self):
        return self.pub_date.strftime('%b %e, %Y')
