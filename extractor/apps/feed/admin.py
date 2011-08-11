from django.contrib import admin
from feed.models import Entity, Feed, FeedItem

class FeedAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Entity)
admin.site.register(Feed, FeedAdmin)
admin.site.register(FeedItem)