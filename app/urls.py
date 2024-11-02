from django.urls import path
from .views.funcViews import homePage
from .views.classViews import StudentListView


urlpatterns = [
    path('function/', homePage, name='students'),
    path('class/', StudentListView.as_view(), name='students_class'),
]