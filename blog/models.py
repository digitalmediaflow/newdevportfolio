from django.db import models

# Create your models here.


class Blog(models.Model):
   title = models.CharField(max_length=255)
   date = models.DateTimeField(auto_now_add = True)
   description = models.TextField()
   image = models.ImageField(upload_to="images/")
