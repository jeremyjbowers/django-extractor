#!/usr/bin/env python
import datetime, feedparser, os, string, urllib2
from datetime import timedelta
from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify, urlize, striptags, escape
from extractor.apps.feed.models import Feed, FeedItem
import simplejson as json

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        '''
        Defines a function which passes content to a Trove API for entity extraction.
        '''
        for item in FeedItem.objects.filter(guid="true")[:1]:
            
            print item.trove_url
            
            response = urllib2.urlopen(item.trove_url)
            my_json = response.read()
            
            print my_json