from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^logging_info_1/(?P<client_id>[a-zA-Z0-9_.-]+)', views.LoggingInfoOne, name='logging_info_1'),
    #url(r'^logging_info_1/$', views.LoggingInfoOne, name='logging_info_1'),
    url(r'^title_description/(?P<client_id>[a-zA-Z0-9_.-]+)$', views.TitleAndDescription, name = 'title_description'),
    url(r'^short_questions/$', views.ShortQuestions, name='short_questions'),
    url(r'^log_all_info/$', views.LogAllInfo, name='log_all_info'),
]