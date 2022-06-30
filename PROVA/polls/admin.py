from django.contrib import admin

# Register your models here.

from .models import The_lord_of_ring,Author,Harry_Potter,The_Chronicles_of_Narnia,Star_War,Hunger_Game


admin.site.register(Author)
admin.site.register(Harry_Potter)
admin.site.register(The_lord_of_ring)
admin.site.register(The_Chronicles_of_Narnia)
admin.site.register(Star_War)
admin.site.register(Hunger_Game)