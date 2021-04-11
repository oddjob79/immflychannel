# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from main.models import Channel, Content, ContentMeta
from urllib.parse import urlparse

def build_content_url(channel_id, absolute_uri):
    # look for channel id in content
    conts = Content.objects.filter(channel_id__exact=channel_id).all()
    content = []
    for con in conts:
        # replace with content and content id
        content_url = absolute_uri+"contents/"+str(con.id) if con else None
        content.append({
            'content_url': content_url
        })
    return content

# route for all channel requests
def all_channels(request):
    # retrieve all channels
    chans = Channel.objects.all()
    # set empty list to populate with channel info
    channels = []
    for chan in chans:
        # build url for accessing parent url
        parent_url = request.build_absolute_uri()+"/"+str(chan.parent_channel_id) if chan.parent_channel is not None else None
        # buld path to show pictures
        pic = urlparse(request.build_absolute_uri(chan.picture))
        # build link to associated contents
        content = build_content_url(chan.id, request.build_absolute_uri()[:-10])
        # populate channels list with channel information
        channels.append({
            'id': chan.id,
            'title': chan.title,
            'language': chan.language,
            'picture_path': pic.path[15:],
            'parent_url': parent_url,
            'content': content
        })

    # build and return json
    return JsonResponse({
        'success': True,
        'channels': channels
    })

# route for specific channel GET requests
def channel(request, id):
    # retrieve channel
    chan = Channel.objects.get(id__exact=id)
    # build url for accessing parent url (strip off channel id from url)
    absolute_uri = request.build_absolute_uri()[:-(len(str(chan.id))+1)]
    parent_url = absolute_uri+"/"+str(chan.parent_channel_id) if chan.parent_channel is not None else None
    # buld path to show pictures
    pic = urlparse(request.build_absolute_uri(chan.picture))
    # build link to associated contents
    content = build_content_url(chan.id, request.build_absolute_uri()[:-10])

    # build and return json
    return JsonResponse({
        'success': True,
        'id': chan.id,
        'title': chan.title,
        'language': chan.language,
        'picture_path': pic.path[15:],
        'parent_url': parent_url,
        'content': content
    })

# Retrieve Content MetaData for content
def retrieve_content_meta(content_id):
    content_meta=[]
    contentmeta = ContentMeta.objects.filter(content_id__exact=content_id)
    for cm in contentmeta:
        content_meta.append({
            'meta_key': cm.meta_key,
            'meta_value': cm.meta_value
        })
    return content_meta

# Build special content for returning to api
def parse_content_data(con, request):
    # build url for accessing channel (strip off contents from url)
    absolute_uri = request.build_absolute_uri()[:-10]
    channel = absolute_uri+"channels/"+str(con.channel_id) if con.channel is not None else None
    # buld path to show content
    image = urlparse(request.build_absolute_uri(con.content))
    # get content metadata
    content_meta = retrieve_content_meta(con.id)
    return channel, image, content_meta

# route for all content GET requests
def all_contents(request):
    conts = Content.objects.all()
    contents = []
    for con in conts:
        channel, image, content_meta = parse_content_data(con, request)
        # populate channels list with channel information
        contents.append({
            'id': con.id,
            'name': con.name,
            'content': image.path[15:],
            'rating': str(con.rating),
            'channel': channel,
            'metadata': content_meta
        })

    # build and return json
    return JsonResponse({
        'success': True,
        'contents': contents
    })

# rouute for specific content GET requests
def content(request, id):
    # retrieve content info
    con = Content.objects.get(id__exact=id)
    # parse con data
    channel, content, content_meta = parse_content_data(con, request)
    # build and return json
    return JsonResponse({
        'id': con.id,
        'name': con.name,
        'content': content.path[15:],
        'rating': str(con.rating),
        'channel': channel,
        'metadata': content_meta
    })
