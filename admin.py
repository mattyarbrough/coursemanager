from django.contrib import admin
from .models import Course, Location, Category, Spot, Session

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"course_slug": ("course_name","session_id",)}
    fieldsets = [
        (None,               {'fields': ['session_id','course_name', 'course_slug', 'course_instructor', 'course_category_id', 'course_description']}),
        ('Date information', {'fields': ['course_start_time', 'course_end_time', 'course_days_of_week', 'course_all_day', 'custom_start_date', 'custom_end_date']}),
        ('Logistics', {'fields': ['course_private', 'course_spaces', 'course_price', 'location_id', 'recurs', 'recurs_interval', 'recurs_times']}),
    ]

admin.site.register(Course, CourseAdmin)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Spot)
admin.site.register(Session)


