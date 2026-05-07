from django.contrib import admin
from .models import Project, Skill, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_type', 'is_featured', 'order', 'updated_at')
    list_display_links = ('title',)
    list_editable = ('is_featured', 'order')
    list_filter = ('project_type', 'is_featured')
    search_fields = ('title', 'summary', 'tools_used')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Identity', {
            'fields': ('title', 'slug', 'summary', 'project_type', 'is_featured', 'order'),
        }),
        ('Detail', {
            'fields': (
                'business_problem', 'tools_used', 'key_features',
                'my_role', 'biggest_challenge', 'what_i_learned',
            ),
        }),
        ('Media', {
            'fields': ('screenshot', 'video', 'video_url', 'downloadable_file'),
        }),
        ('Links', {
            'fields': ('github_link', 'live_demo_link'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'category')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'timestamp', 'is_read')
    list_display_links = ('subject',)
    list_editable = ('is_read',)
    list_filter = ('is_read',)
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('name', 'email', 'subject', 'message', 'timestamp')

    def has_add_permission(self, request):
        # Contact messages are created by the public form, not the admin
        return False
