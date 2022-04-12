from django.db import models

class Animal(models.Model):
    avatar = models.TextField("Link to the photo")
    bio = models.TextField("Bio")
    firstname = models.CharField("First name", max_length=30)
    lastname = models.CharField("Last name", max_length=30)
    title = models.CharField(max_length=30)

    def get_absolute_url(self):
        return f'/{self.id}'