from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from comentarios import views


urlpatterns = [
	url(r'^comentarios/$', views.ComentarioList.as_view(), name="comentarios"),
	
]

"""
urlpatterns = patterns('',
	url(r'^comentarios/$', views.ComentarioList.as_view(), name="comentarios"),
	url(r'^comentarios/(?P&lt;pk&gt;[0-9]+)/$', views.ComentarioDetail.as_view(), name="comentarios-detail"),
	url(r'^$', views.ComentarioView.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
"""