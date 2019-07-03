from django.contrib import admin
from django.urls import path
from ticket import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url

from django.conf.urls.static import static
from ticket_booking import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('reg/',views.reg,name='reg'),
    path('forgot/',views.forgot,name='forgot'),
    path('logout/',views.logout,name='logout'),
    path('sample/', views.sample, name='sample'),

# --------------------- Customer -------------------

    path('custhome/',views.custhome,name='custhome'),
    path('custmovie/',views.custmovie,name='custmovie'),
    url(r'^custloc/(?P<prod_id>[0-9]+)/$', views.custloc, name='custloc'),
    path('custloc2/',views.custloc2,name='custloc2'),
    path('custslot/',views.custslot,name='custslot'),
    path('custconfirm/',views.custconfirm,name='custconfirm'),
    path('custack/',views.custack,name='custack'),
    path('custprofile/',views.custprofile,name='custprofile'),
    path('custnoti/',views.custnoti,name='custnoti'),
    path('custcancel/',views.custcancel,name='custcancel'),
# --------------------- Theatre ---------------------

    path('thehome/',views.thehome,name='thehome'),
    path('theadd/',views.theaddmovies,name='theadd'),
    path('thecust/',views.thecusthis,name='thecusthis'),
    path('theprofile/',views.theprofile,name='theprofile')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)