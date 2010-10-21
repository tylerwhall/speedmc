from django.conf.urls.defaults import *
import speedmc.settings

urlpatterns = patterns('',
    (r'^joinserver.jsp', 'speedmc.mcauth.views.joinserver'),
    (r'^checkserver.jsp', 'speedmc.mcauth.views.checkserver'),
    (r'^getversion.jsp', 'speedmc.mcauth.views.getversion'),
)
