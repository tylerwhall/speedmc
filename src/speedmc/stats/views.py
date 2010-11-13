# Create your views here.
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
import xmlrpclib

def getProxy():
    return xmlrpclib.ServerProxy("http://user:password@evanwilliams:20012")

def getPlayers():
    p = getProxy()
    try:
        return p.player.getPlayers()
    except IOError:
        return None

def getStats():
    p = getProxy()
    stats = [
        ('MOTD', p.server.getMotd()),
        ('Player Count', p.server.getPlayerCount()),
        ('Player Limit', p.server.getPlayerLimit()),
        ('Disallowed Items', p.server.getDisallowedItems()),
        ('Hey0 Plugins', ','.join([pl['id'] for pl in p.server.getPlugins()])),
    ]
    return stats

def links():
    return [
        (reverse(players), 'Users Logged On'),
        (reverse(home), 'Server Stats'),
        (reverse(home), 'Minecraft Stats'),
    ]

def home(request):
    d = {"links": links()}
    try:
        d['stats'] = getStats()
    except IOError:
        pass
    return render_to_response('stats/home.html', d)

def players(request):
    d = {"links": links()}
    try:
        d['players'] = getPlayers()
    except IOError:
        pass
    return render_to_response('stats/players.html', d)
