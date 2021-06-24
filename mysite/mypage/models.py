from django.db import models

# Create your models here.

class Description(models.Model):
    txt_description = models.CharField(max_length=500)
    #profile_pic = models.ImageField(upload_to="profile_pics")
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.txt_description