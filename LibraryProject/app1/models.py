from django.db import models

# Create your models here.
class Books(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    desc=models.CharField(max_length=600)
    year=models.IntegerField()
    image=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name
