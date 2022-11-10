from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    # path('detail',views.details,name='details')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:taskid>/',views.update,name='update'),
    #class based view
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdelete')
]