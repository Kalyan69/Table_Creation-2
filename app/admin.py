from django.contrib import admin


from app.models import *

# Register your models here.


admin.site.register(Blog)

admin.site.register(Author)

admin.site.register(Entry)