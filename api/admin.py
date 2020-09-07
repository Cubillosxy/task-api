from django.contrib import admin
from api.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'description', 'done')
    search_fields = ('user__username', 'user__email', 'description')
    list_filter = ('done',)
    readonly_fields = ('created_at', )
