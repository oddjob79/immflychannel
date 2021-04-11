from django.contrib import admin
from .models import Channel, Content, ContentMeta

class ContentMetaAdminInline(admin.TabularInline):
    model = ContentMeta

class ContentAdmin(admin.ModelAdmin):
    inlines = (ContentMetaAdminInline,)

admin.site.register(Channel)
admin.site.register(Content, ContentAdmin)
