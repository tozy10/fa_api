from django.db import models

class trapImage(models.Model):
    count = models.IntegerField()
    timeStamp = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/")
