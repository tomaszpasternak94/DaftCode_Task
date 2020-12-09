from django.db import models

# Create your models here.

class Crud(models.Model):
    message = models.CharField(max_length=160)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.message

