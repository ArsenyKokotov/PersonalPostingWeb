from django.db import models

# Create your models here.

class Description(models.Model):
    txt_description = models.CharField(max_length=500)

    def __str__(self):
        return self.txt_description