from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from product_app import views


urlpatterns = [
	url(r'^product_app/$', views.ProductList.as_view(), name="produtos"),
	
]

"""
urlpatterns = patterns('',
	url(r'^product_app/$', views.ProductList.as_view(), name="produtos"),
	url(r'^product_app/(?P&lt;pk&gt;[0-9]+)/$', views.ProductDetail.as_view(), name="produtos-detail"),
	url(r'^$', views.ProductView.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)

"""