from django.conf.urls import url
from bookshop import views

urlpatterns = [
	url(r'^books/$', views.book_list, name='book_list'),
	url(r'^books/(?P<pk>[0-9]+)/$', views.book_detail, name='book_detail'),
	url(r'^authors/$', views.author_list, name='author_list'),
	url(r'^authors/(?P<pk>[0-9]+)/$', views.author_detail, name='author_detail'),
]

