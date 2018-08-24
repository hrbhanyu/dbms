from django.contrib import admin

# Register your models here.
from unifieddbms.models import host_info,database_info
admin.site.register([host_info,database_info])
