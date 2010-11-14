# Create your views here.
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
import xmlrpclib

def getProxy():
    return xmlrpclib.ServerProxy("http://user:password@evanwilliams:20012")

def getServerInfo():
    p = getProxy()
    stats = [
        ('MOTD', p.server.getMotd()),
        ('Player Count', p.server.getPlayerCount()),
        ('Player Limit', p.server.getPlayerLimit()),
        ('Disallowed Items', p.server.getDisallowedItems()),
        ('Hey0 Plugins', ','.join([pl['id'] for pl in p.server.getPlugins()])),
    ]
    players = p.player.getPlayers()
    return stats, players

def getPlayerInventory(player):
    p = getProxy()
    i = p.player.getInventory(player)
    return [(k, i[k]) for k in sorted(i.keys(), key=lambda x:int(x))]

def home(request):
    d = {}
    try:
        d['stats'], d['players'] = getServerInfo()
    except IOError:
        pass
    return render_to_response('stats/home.html', d)

def player(request, name):
    d = {}
    d['playername'] = name
    try:
        d['inventory'] = getPlayerInventory(name)
    except IOError:
        pass
    except xmlrpclib.Fault:
        d['notonline'] = True

    return render_to_response('stats/player.html', d)
