from django.db import models
from extractor.apps.models import ModelBase
from django.template.defaultfilters import slugify

class Feed(ModelBase):
    name                = models.CharField(max_length=255)
    url                 = models.CharField(max_length=255)
    subject             = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.feed_name
    
    def get_related_feeditems(self):
        related         = FeedItem.objects.filter(feed=self)
        return related
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(Feed, self).save(*args, **kwargs)
    

class FeedItem(ModelBase):
    feed                = models.ForeignKey(Feed)
    headline            = models.CharField(max_length=255)
    content             = models.TextField()
    permalink           = models.URLField()
    publication_date    = models.DateTimeField()
    guid                = models.CharField(max_length=255, blank=True, null=True)
    lead_image_url      = models.CharField(max_length=255, blank=True, null=True)
    
    def __unicode__(self):
        return "%s: %s" % (self.feed.feed_name, self.headline)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(FeedItem, self).save(*args, **kwargs)