from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse


from django.contrib.auth.decorators import login_required
from app.models import Sufficiency

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'legalsuff.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^list/$', login_required(ListView.as_view(template_name="sufficiency_list.html", queryset=Sufficiency.objects.order_by("measure_type")))),
    url(r'^add/$', 'app.views.add_memo', name='add'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^show_sufficiency/(?P<sufficiency_id>[0-9]+)/$', 'app.views.show_sufficiency', name='show_sufficiency'),

)
