#!/usr/bin/env python
import datetime, feedparser, os, string, urllib2, re
from datetime import timedelta
from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify, urlize, striptags, escape
from extractor.apps.feed.models import Feed, FeedItem
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        '''
        Defines a function which scrapes the permalink URLs for RSS items to get body text.
        '''
        for item in FeedItem.objects.filter(guid="false"):
            try:
                response = urllib2.urlopen(item.xml_url)
                html = response.read()
                
                soup = BeautifulSoup(html)
                body = striptags(soup.findAll(re.compile('^ece:field'))[0])
                body = body.replace("\n", "").replace("\r", "")
                item.content = body
                item.guid = "true"
                item.save()
                print "Updated %s" % item
            except:
                print "Turns out, this isn't a story."
        
        for item in FeedItem.objects.filter(guid="true"):
            response = urllib2.urlopen(item.xml_url)
            html = response.read()
            
            soup = BeautifulSoup(html)
            try:
                image = soup.findAll(re.compile('^ece:multimediagroup'))[:1][0]
                image = image.findAll(re.compile('^ece:multimedia'))[0]['filename']
                
                item.lead_image_url = image
                item.save()
                print "Imaged %s" % item
            except:
                print "This one doesn't have an image."