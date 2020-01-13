from django.db import models

class   Car(models.Model):
    colour = models.CharField(max_length=64, null=False)
    year = models.IntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=64, null=False, blank=False)
    def __str__(self):
        return (self.manufacturer)