from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=255)
    desription = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name +' '+ self.desription
