from django.contrib import admin
from .models import Author, Tags, Quotes

# Register your models here.
admin.site.register(Author)
admin.site.register(Tags)
admin.site.register(Quotes)
