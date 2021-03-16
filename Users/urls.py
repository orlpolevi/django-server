#API 

from django.conf.urls import url 
from Users import views

urlpatterns = [ 
    url(r'^api/Users/(?P<pk>[0-9]+)$', views.user_get_by_id)
    #url(r'^api/Users$', views.user_get_by_id)
]