from django.conf.urls import url
from app01.views import TestViewer,mainViewer,CollegeViewer,ClassesViewer

urlpatterns = [
   url(r'^test/',TestViewer.test),

   url(r'^index/',mainViewer.index, name='index'),

   url(r'^college/',CollegeViewer.college, name='college'),
   url(r'^addCollege/',CollegeViewer.addCollege,name='addCollege'),
   url(r'^delCollege/',CollegeViewer.delCollege,name='delCollege'),
   url(r'^setCollege/',CollegeViewer.setCollege,name='setCollege'),

   url(r'^classes/',ClassesViewer.classes,name='classes'),
   url(r'^addClass/',ClassesViewer.addClass,name='addClass'),
   url(r'^delClass/',ClassesViewer.delClass,name='delClass'),
   url(r'^setClass/',ClassesViewer.setClass,name='setClass'),
]