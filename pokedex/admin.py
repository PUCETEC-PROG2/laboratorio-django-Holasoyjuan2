from django.contrib import admin
from .models import Pokemon, Trainer

# Register your models here.
@admin.register(Pokemon)
class Pokemonadmin(admin.ModelAdmin):
    pass
# Register your models here.
@admin.register(Trainer)
class TrainerAdmin(admin.TrainerAdmin):
    pass