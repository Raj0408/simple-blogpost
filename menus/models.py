from django.db import models

# Create your models here.


class blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(default='2021-09-01')

    def __str__(self):
        return self.title