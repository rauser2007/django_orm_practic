from django.db import models

# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=15)

class Task(models.Model):
    title = models.CharField(max_length=50)
    descrition = models.TextField()
    user = models.ForeignKey("users_and_roles.user", on_delete=models.CASCADE)

    