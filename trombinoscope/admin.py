from django.contrib import admin
from .models import Trombinoscope,Member,Department,Role,Category

# Register your models here.


admin.site.register(Trombinoscope)
admin.site.register(Member)
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Category)