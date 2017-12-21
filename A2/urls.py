"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "A2"
"""
router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
"""


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^notloggedin$', views.notloggedin, name='notloggedin'),
    url(r'^index$', views.index, name='index'),
    url(r'^help$', views.help, name='help'),
    url(r'^addtask$', views.addtask, name='addtask'),
    url(r'^edittask$', views.edittask, name='edittask'),
    url(r'^edittask/(?P<task_id>\d+)$', views.edittask, name='edittask'),
    url(r'^removetask/(?P<task_id>\d+)$', views.removetask, name='removetask'),
    url(r'^clearlist$', views.clearlist, name='clearlist'),
    url(r'^tasks/$', views.task_list),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.task_detail),
    #url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)