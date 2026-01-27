from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin): # uevo​
    list_display = (
    "titulo",
    "autor",
    "cuerpo",
    )

admin.site.register(Post, PostAdmin)
