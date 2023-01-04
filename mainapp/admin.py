from django.contrib import admin

from mainapp.models import News, Courses, CourseTeachers, Lesson


admin.site.register(Courses)
admin.site.register(Lesson)
admin.site.register(CourseTeachers)

@admin.register(News) #второй способ регистрации, расширяющий функционал для админки
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'deleted')
    actions = ('mark_as_delete',)

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'