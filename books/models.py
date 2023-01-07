from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    pages = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    pdf = models.FileField(upload_to='pdf/')

    def __str__(self):
        return self.title