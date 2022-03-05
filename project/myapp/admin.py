from django.contrib import admin
from .models import Flats, Students
# Register your models here.

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    def flat(self):
        return self.student_flat.flat_name
    flat.short_description = "所住公寓"
    # short_description修改列名的显示
    list_display = ['student_number', 'student_name', 'student_gender', 'student_chinese', 'student_math', 'student_english',flat]




@admin.register(Flats)
class FlatAdmin(admin.ModelAdmin):
    list_display = ['flat_id', 'flat_name', 'flat_number', 'flat_teacher','flat_image']