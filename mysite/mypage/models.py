from django.db import models

# Create your models here.

class Description(models.Model):
    #user
    txt_description = models.CharField(max_length=10000)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.txt_description

class Gallery(models.Model):
    #user
    txt = models.CharField(max_length=500)
    new_file = models.FileField(upload_to ='uploaded_files/')
