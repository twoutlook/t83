from django.contrib import admin

# from import_export import resources,fields
# from import_export.admin import ImportExportModelAdmin
from .models import T83


# class T83Resource(resources.ModelResource):
#     class Meta:
#         model = T83
#         fields = ('t83_num', 't83_name','t83_short',)
#
#
# class T83Admin(ImportExportModelAdmin):
#     resource_class = T83Resource

class T83Admin(admin.ModelAdmin):
    fields = ['t83_num', 't83_short','t83_name',]
    list_display = ('t83_num', 't83_short','t83_name',)

admin.site.register(T83, T83Admin)
