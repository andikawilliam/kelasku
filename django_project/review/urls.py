from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.front_page,name='kelasku'),
    path('home/', views.home,name='review-home'),
    path('about/', views.about,name='review-about'),
    path('courses/', views.courses,name='review-courses'),
    url(r'^courses/(?P<course_id>[0-9]+)/$', views.course_detail, name='course_detail'),
    url(r'^courses/(?P<course_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),

    path('weather/', views.campus_weather, name='campus_weather'),
]
