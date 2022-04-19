
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    descriptions = models.CharField(max_length=350)
    image = models.ImageField(upload_to='portfolio/image/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
