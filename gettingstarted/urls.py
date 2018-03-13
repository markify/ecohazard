from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^about$', hello.views.about, name='about'),
    url(r'^about-ali/', hello.views.about1, name='about1'),
    url(r'^about-cameron/', hello.views.about2, name='about2'),
    url(r'^about-girish/', hello.views.about3, name='about3'),
    url(r'^about-humeston/', hello.views.about4, name='about4'),
    url(r'^about-larsen/', hello.views.about5, name='about5'),
    url(r'^about-mark/', hello.views.about6, name='about6'),
    url(r'^about-sutherland/', hello.views.about7, name='about7'),
    path('admin/', admin.site.urls),
]
