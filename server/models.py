from django.db import models


class Server(models.Model):
    url = models.CharField(max_length=120)
    description = models.TextField()
    https = models.BooleanField(default=False)

    def _str_(self):
        return self.title

  # Create your models here.
