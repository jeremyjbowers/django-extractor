from django.db import models
from extractor.apps.models import ModelBase
from django.template.defaultfilters import slugify, urlencode
import re, string

class Entity(ModelBase):
    name                = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(FeedItem, self).save(*args, **kwargs)

class Feed(ModelBase):
    name                = models.CharField(max_length=255)
    url                 = models.CharField(max_length=255)
    subject             = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.name
    
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
    permalink           = models.CharField(max_length=255)
    publication_date    = models.DateTimeField()
    guid                = models.CharField(max_length=255, blank=True, null=True, default="false")
    lead_image_url      = models.CharField(max_length=255, blank=True, null=True)
    entities            = models.ManyToManyField(Entity, blank=True, null=True)
    
    def __unicode__(self):
        return self.permalink
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__()[:199])
        super(FeedItem, self).save(*args, **kwargs)
    
    @property
    def trove_url(self):
        if self.guid == "true":
            return 'http://iddevasyncnews.wapolabs.com/entities/entityExtraction.json?content=%s' % string.strip(urlencode(self.content), "%90")[:2000]
        else:
            return None
    
    @property
    def json_url(self):
        try:
            guid = re.search('/(\w+)_', self.permalink)
            guid = guid.group(1)
            return 'http://www.washingtonpost.com/%s_json.html' % guid
        except:
            return None
    
    @property
    def xml_url(self):
        try:
            guid = re.search('/(\w+)_', self.permalink)
            guid = guid.group(1)
            return 'http://www.washingtonpost.com/%s_mobile.html' % guid
        except:
            return None