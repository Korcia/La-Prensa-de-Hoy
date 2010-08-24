from django.conf.urls.defaults import *
import settings 

urlpatterns = patterns('accounts.views',
    (r'^register/$', 'register', 
        {'template_name': 'registration/register.html' }, 'register'),
    (r'^mi_cuenta/$', 'my_account', 
         {'template_name': 'registration/my_account.html'}, 'my_account'),
    (r'^order_info/$', 'order_info', 
         {'template_name': 'registration/order_info.html'}, 'order_info'),
    (r'^order_details/(?P<order_id>[-\w]+)/$', 'order_details', 
         {'template_name': 'registration/order_details.html'}, 'order_details'),
)

urlpatterns += patterns('django.contrib.auth.views',
    (r'^login/$', 'login', 
     {'template_name': 'registration/login.html' }, 'login'),
)

urlpatterns += patterns('django.contrib.auth.views',
    (r'^logout/$', 'logout', 
     {'template_name': 'registration/logout.html' }, 'logout'),
)