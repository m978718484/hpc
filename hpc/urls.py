from django.test import TestCase

# Create your tests here.
from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$',views.index),
	url(r'Overview/',views.Overview),
	url(r'News/',views.News),
	url(r'Trends/',views.Trends),
	url(r'Projects/',views.Projects),
	url(r'graduate/',views.graduate),
	url(r'Friend/',views.Friend),
	url(r'Services/',views.Services),
	url(r'statistics/',views.statistics),
	url(r'SourceDown/',views.SourceDown),
	url(r'Experience/',views.Experience),
	url(r'ModelApp/',views.ModelApp),
	url(r'faq/',views.faq),
]