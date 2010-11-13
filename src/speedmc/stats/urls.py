from django.conf.urls.defaults import patterns, url
import speedmc.settings
from views import home, players

urlpatterns = patterns('',
    #(r'^$', 'speedmc.stats.views.home'),
    url(r'^$', home),
    url(r'^players$', players),
)
