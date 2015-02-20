
from django.conf.urls import patterns, include, url
from .views import ExperienceListAPIView, BioListAPIView, ExperienceRetrieveUpdateDestroyAPIView, BioUpdateAPIView, ExperienceAPIView
from django.contrib import admin
from django.conf.urls import include



urlpatterns = patterns('',

    url(r'^experience/$', ExperienceAPIView.as_view()),
    url(r'^experience/add/$', ExperienceListAPIView.as_view()),
    url(r'^experience/change/(?P<experience_id>\d+)/$', ExperienceRetrieveUpdateDestroyAPIView.as_view(), name='delete_patch_experience'),



    url(r'^bio/$', BioListAPIView.as_view()),
    url(r'^bio/change/(?P<owner_id>\d+)/$', BioUpdateAPIView.as_view(), name='patch_bio'),
    # url(r'^(?P<todo_id>\d+)/details/$', TodoDetailAPIView.as_view(), name='todo-detail'),
    #
    # url(r'^create/$', TodoCreateAPIView.as_view()),
    #
    # url(r'^filter/$', TodoFilterListAPIView.as_view()),
    # url(r'^serializer/$', TodoListModifySerializerAPIView.as_view()),
    # url(r'^todoactivity/$', TodoActivityDetailAPIView.as_view()),
    #
    # url(r'^users/$', UserList.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


)