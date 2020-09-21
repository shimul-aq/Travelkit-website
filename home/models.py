from django.db import models

class Destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Contact(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    message = models.TextField()

    def __str__(self):
        return self.name
    

