from django.db import models

# Create your models here.


class Superhero(models.Model):
    hero_name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_ability = models.CharField(max_length=50)
    secondary_ability = models.CharField(max_length=50)
    catchphrase = models.CharField(max_length=60)
    hero_image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.hero_name
