from django.conf import settings
from django.db import models



class Task(models.Model):

    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=200)
    text = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
        null=True
        
    )

    def publish(self):
        self.save()

    def __str__(self):
        return self.title