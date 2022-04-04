from django.contrib import admin
from .models import student,Department,Subject,Examination

# Register your models here.
admin.site.register(student)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Examination)