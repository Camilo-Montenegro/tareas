from django.contrib import admin

from .models import Task

@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_created', 'created')
    search_fields = ('title',{'created', 'is_created'})
    list_filter = ('is_created', 'created')
    ordering = ('-created',)
