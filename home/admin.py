from django.contrib import admin
from .models import Student

admin.site.register(Student)

# Customize the admin site header and titles
admin.site.site_header = "My Custom Admin Panel"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Welcome to the Custom Admin Panel"
