from django.contrib import admin
from .models import Startup, Investor, Contact

# Register your models here.
admin.site.register(Startup)
admin.site.register(Investor)
admin.site.register(Contact)