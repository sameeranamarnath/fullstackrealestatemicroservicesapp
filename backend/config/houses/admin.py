from django.contrib import admin

# Register your models here.

from .models import House
from .models import Checker

admin.site.register(House)
admin.site.register(Checker)
