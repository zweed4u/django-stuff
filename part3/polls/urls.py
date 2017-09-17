from django.conf.urls import url
from . import views

urlpatterns = [
	# /polls/
	url(r'^$', views.index, name="index"),
	
	# /polls/<id>/ - 'name' value as called by url template tag
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),

	#added the word specifics to url
	url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name="detail"),

	# /polls/<id>/results/
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"),

	# /polls/<id>/vote
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
]
