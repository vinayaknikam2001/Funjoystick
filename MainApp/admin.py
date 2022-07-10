from django.contrib import admin
from .models import Contact,Game,Playgame


# Register your models here.
admin.site.register(Contact)
admin.site.register(Game)
admin.site.register(Playgame)