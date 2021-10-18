from django.contrib import admin
from django.db import models
from .models import menus
from .models import photos

admin.site.register (menus)

admin.site.register(photos)


