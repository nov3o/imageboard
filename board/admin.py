from django.contrib.admin import AdminSite

from .models import Post, Thread

class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Post)
admin_site.register(Thread)