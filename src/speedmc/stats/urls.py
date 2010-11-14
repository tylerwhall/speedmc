from django.conf.urls.defaults import patterns, url
import speedmc.settings
from views import home, player

urlpatterns = patterns('',
    #(r'^$', 'speedmc.stats.views.home'),
    url(r'^$', home),
    url(r'^player/(?P<name>[^/]+)', player),
)
