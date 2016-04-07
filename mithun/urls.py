from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.hello,name='hello'),
	url(r'^hello/',views.hello,name='hello'),
	url(r'^hello1/',views.hello1,name='hello1'),
	url(r'^crudops/',views.crudops,name='crudops'),
	url(r'^crudops1/',views.crudops1,name='crudops1'),
	url(r'^cr/',views.cr,name='cr'),
	url(r'^cr/',views.cr,name='cr'),
	url(r'^hi/',views.hi,name='hi'),
	url(r'^hi1/(\d+)/(\d+)/',views.hi1,name='hi1'),
]

