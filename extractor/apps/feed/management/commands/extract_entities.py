#!/usr/bin/env python
import datetime, feedparser, os, string
from datetime import timedelta
from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify, urlize, striptags, escape
from extractor.apps.feed.models import Feed, FeedItem

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        '''
        Defines a function which extracts entities from captured feed items.
        '''
        
        feed_items = FeedItem.objects.all()
        
        for item in feed_items:
            
            # Do the magic.
            pass