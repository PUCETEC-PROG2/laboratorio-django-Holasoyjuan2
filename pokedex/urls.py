from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("trainer/<int:trainer>/", views.trainer_detail, name="trainer"),
]