from django.contrib import admin

# Register your models here.
from .models import Movie, Showtime, Booking

admin.site.register(Movie)
admin.site.register(Showtime)
admin.site.register(Booking)
