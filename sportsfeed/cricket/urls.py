from django.conf.urls import url,patterns

from cricket import views

urlpatterns = patterns('',
	url(r'^$',views.index,name="index"),
	url(r'^news/',views.news,name="news"),
	url(r'^(?P<l_id>\d+)/$',views.localmatch,name="localmatch"),
	) 
