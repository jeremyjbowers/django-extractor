#!/usr/bin/env python
import datetime, feedparser, os, string
from datetime import timedelta
from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify, urlize, striptags, escape
from extractor.apps.feed.models import Feed, FeedItem

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        '''
        Defines a function which fetches RSS feed items.
        '''
        
        feeds = Feed.objects.filter(active=True)
        
        # Deactivate old feed items in preparation for replacing them with newer ones.
        if feeds.count() > 0:
            for feed in feeds:
                
                parsed_feed = feedparser.parse(feed.url)                
                for entry in parsed_feed.entries:
                    try:
                        f = FeedItem.objects.get(permalink=entry.guid.encode('utf-8'))
                        f.headline=entry.title.encode('utf-8')
                        f.content=entry.description.encode('utf-8')
                        f.publication_date=datetime.datetime(
                            entry.date_parsed[0], 
                            entry.date_parsed[1], 
                            entry.date_parsed[2], 
                            entry.date_parsed[3], 
                            entry.date_parsed[4], 
                            entry.date_parsed[5]
                        )-timedelta(hours=7)
                        print u'* %s' % (f)
                    except:
                        f = FeedItem(
                            feed=feed,
                            active=True,
                            permalink=entry.guid.encode('utf-8'),
                            headline=entry.title.encode('utf-8'),
                            content=entry.description.encode('utf-8'),
                            publication_date=datetime.datetime(
                                entry.date_parsed[0], 
                                entry.date_parsed[1], 
                                entry.date_parsed[2], 
                                entry.date_parsed[3], 
                                entry.date_parsed[4], 
                                entry.date_parsed[5]
                            )-timedelta(hours=7)
                        )
                        f.save()
                        print u'+ %s' % (f)
                            