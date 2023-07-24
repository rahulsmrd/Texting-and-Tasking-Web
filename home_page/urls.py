from django.urls import path
from home_page import views


app_name='home_page'

urlpatterns =[
    path('',views.home_page_view,name="home_page"),
    path('tasks/',views.TasksView, name="tasks"),
    path('taskdetail/<pk>/',views.taskDetail,name='taskdetail'),
    path('taskdelete/<pk>/',views.TaskDelete.as_view(),name='delete'),
    path('newtask/',views.NewTask, name="newtask"),
    path('messages/',views.MessageView, name="messages"),
    path('messagedetail/<pk>/',views.message_detail_view,name='messagedetail'),
    path('newMessage/',views.CreateMessage,name='newmessage'),
]