from django.db import models

# Create your models here.
class Pokemon(models.Model):

    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPES = {
        ('A', 'Agua'),
        ('F', 'Fuego'),
        ('T', 'Tierra'),
        ('P', 'Planta'),
        ('E', 'Elctrico'),
        ('L', 'Lgartija'),
    }       
    type = models.CharField(max_length=30, choices=POKEMON_TYPES, null=False)
    weight = models.DecimalField(decimal_places=4, max_digits=6)
    height = models.DecimalField(decimal_places=4, max_digits=6)
    
    def __str__(self):
        return self.name
    
class Trainer(models.Model):
    
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField()
    level = models.IntegerField(default=1)
    def __str__(self):
        return f'{self.first_name}{self.last_name}'
        