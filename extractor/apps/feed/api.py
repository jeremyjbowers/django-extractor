from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.api import Api
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from feed.models import FeedItem, Entity, Feed
from django.template.defaultfilters import truncatewords

class FeedResource(ModelResource):
    class Meta:
        queryset = Feed.objects.all()
        resource_name = "feeds"
        filtering = {
            'subject'                               : ALL_WITH_RELATIONS,
        }

class FeedItemResource(ModelResource):
    feed = fields.ForeignKey(FeedResource, 'feed', full=True)
    class Meta:
        queryset = FeedItem.objects.filter(active=True).order_by('-publication_date')
        resource_name = 'feed_items'
        filtering = {
            'publication_date'                      : ALL_WITH_RELATIONS,
            'feed'                                  : ALL_WITH_RELATIONS,
        }
        allowed_methods = ['get']
    

class RandomFeedItemResource(ModelResource):
    feed = fields.ForeignKey(FeedResource, 'feed', full=True)
    short_content = fields.CharField()
    class Meta:
        queryset = FeedItem.objects.filter(guid="true").order_by('?')[:1]
        resource_name = "random"
        allowed_methods = ['get']
    
    def dehydrate_short_content(self, bundle):
        return truncatewords(bundle.obj.content, 50)

v1 = Api(api_name='v1')

v1.register(FeedItemResource())
v1.register(FeedResource())
v1.register(RandomFeedItemResource())