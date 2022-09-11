from django.db import models

class studentModel(models.Model):
        name = models.CharField(max_length=255)
        roll = models.CharField(max_length=255)
