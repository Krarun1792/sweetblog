from django.conf.urls import url,include
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.blog_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.blog_detail, name="detail"),
    

]
