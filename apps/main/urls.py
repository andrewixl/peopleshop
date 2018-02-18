from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^categories/(?P<id>\w+)/$', views.categories),
    url(r'^product/(?P<type_id>\w+)/(?P<product_id>\d+)/$', views.product),
    url(r'^promotions/$', views.promotions),
    url(r'^contact/$', views.contact, name='website_contact'),
]
