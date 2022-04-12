from django.db import models

class Animal(models.Model):
    avatar = models.TextField("Link to the photo", default="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQSRpiKVmDu4KctY07T_FzEnYkdYFBCwoqU2NDlNc6HKej9jXHjZQ")
    bio = models.TextField("Bio")
    firstname = models.CharField("First name", max_length=30)
    lastname = models.CharField("Last name", max_length=30)
    title = models.CharField(max_length=30)

    def get_absolute_url(self):
        return f'/{self.id}'