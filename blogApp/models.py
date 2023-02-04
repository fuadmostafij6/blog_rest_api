from django.db import models


# Create your models here.

class BlogModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    details = models.CharField(max_length=1200,)
    user = models.CharField(max_length=50)

    def __str__(self):

        return f"{self.user}--{self.title}"
