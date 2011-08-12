from django.shortcuts import redirect
from feed.models import FeedItem

def random(request):
    random_item = FeedItem.objects.filter(guid='true').order_by('?')[:1][0]
    return redirect(random_item.permalink)