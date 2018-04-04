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
    url(r'^about(-\w*)?/?$', hello.views.about, name='about'),
    url(r'^map(?:\.html?)?/?$', hello.views.map, name='map'),
    url(r'^signup', hello.views.signup, name='signup'),
    url(r'^login', hello.views.login, name='login'),
    url(r'^report', hello.views.post_report, name='report'),
    url(r'^process_new_report', hello.views.process_new_report, name='process_new_report'),
    url(r'^search', hello.views.search, name='search'),
    path('admin/', admin.site.urls),
]

