from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='homepage'),
    path('home/',views.home,name='homepage'),
    path('complete/<int:id>/',views.complete_task,name='completepage'),
    path('completed/',views.completed_tasks,name='completedpage'),
    path('incomplete/',views.incomplete_tasks,name='incompletepage'),
    path('edit_task/<int:id>/',views.edit_task,name='editpage'),
    path('delete_task/<int:id>/',views.delete_task,name='deletepage'),
    path('deleted_task/<int:id>/',views.deleted_task,name='deletedpage'),
    path('add_task/',views.add_tasks,name='addpage'),
    path('signup/',views.sign_up,name='signup'),
    path('log_in/',views.log_in,name='login'),
    path('log_out/',views.log_out,name='logout'),
    path('search/', views.task_search, name='task_search'),
    path('order/', views.task_ordering, name='task_order'),
    path('profile/', views.edit_profile, name='profile'),
      
]
