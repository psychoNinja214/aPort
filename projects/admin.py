from django.contrib import admin
from .models import Project, Technology


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']
    search_fields = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'featured', 'order', 'created_at']
    list_editable = ['status', 'featured', 'order']
    list_filter = ['status', 'featured', 'technologies']
    search_fields = ['title', 'tagline', 'description']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['technologies']
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'tagline', 'description', 'image')
        }),
        ('Technologies & Links', {
            'fields': ('technologies', 'live_url', 'github_url')
        }),
        ('Display', {
            'fields': ('status', 'featured', 'order')
        }),
    )
