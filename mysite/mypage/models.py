from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Description(models.Model):
    #user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="description", null=True)
    txt_description = models.TextField(max_length=10000)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.txt_description

class Gallery(models.Model):
    #user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gallery", null=True)
    name = models.CharField(max_length=20, null=False)
    txt = models.CharField(max_length=500, null=True)
    new_file = models.FileField(upload_to ='uploaded_files/')

    class Meta:
        constraints= [models.UniqueConstraint(
            fields=['user', 'name'],
            name='unique file name'
        )]
