from django.contrib import admin
from .models import Post, Author, Tag



class SiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("title", "tags")    
    list_display = ("title",)
    
    
# Register your models here.
admin.site.register(Post, SiteAdmin)
admin.site.register(Author)
admin.site.register(Tag)
