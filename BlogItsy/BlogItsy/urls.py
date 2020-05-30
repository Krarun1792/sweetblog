from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    # url(r'^(?P<slug>[\w-]+)/$', views.home, name="detail1"),
    url(r'^about/$', views.about, name="about"),
    url(r'^blog/$', views.blog,),
    url(r'^contact/$', views.contact,name="contact"),
    url(r'^articles/', include('articles.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
