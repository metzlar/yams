from django.db import models


class Machine(models.Model):
    name = models.CharField(max_length=25)
    ip = models.CharField(max_length=15)
    last_known_state = models.CharField(max_length=5)