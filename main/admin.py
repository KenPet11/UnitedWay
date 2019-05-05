from django.contrib import admin
from .models import Event
from .models import Signup
from django.db import models

# Register your models here.

admin.site.register(Event)
admin.site.register(Signup)