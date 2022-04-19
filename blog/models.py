from time import timezone
from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=250)
    description = models.TextField(default='')
    date = models.DateTimeField()

    def __str__(self):
        return self.title
