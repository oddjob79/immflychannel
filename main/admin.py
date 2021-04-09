from django.contrib import admin
from .models import Channel, Content, ContentMeta

class ContentMetaAdminInline(admin.TabularInline):
    # list_display = ('meta_key', 'meta_value')
    # list_display_links = ('meta_key', 'meta_value')
    # # list_editable = ('meta_key', 'meta_value')
    model = ContentMeta

class ContentAdmin(admin.ModelAdmin):
    # fields = ('name', 'content', 'rating')
    inlines = (ContentMetaAdminInline,)

admin.site.register(Channel)
admin.site.register(Content, ContentAdmin)
# admin.site.register(ContentMeta, ContentMetaAdmin)
