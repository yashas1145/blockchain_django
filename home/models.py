from django.db import models

# Create your models here.

class Block(models.Model):
    
    data = models.CharField(max_length=200)
    hash = models.CharField(max_length=500)
    prev_hash = models.CharField(max_length=500)

    def __str__(self):
        return "Data: '{}' with hash {}".format(self.data, self.hash)