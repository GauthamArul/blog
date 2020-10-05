from django.db import models
from django.contrib.auth.models import User


class Picture(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    picture_file = models.ImageField()
    creator = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
