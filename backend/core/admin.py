from django.contrib import admin
from .models import Application, Server, Database, Service

admin.site.register(Application)
admin.site.register(Server)
admin.site.register(Database)
admin.site.register(Service)
