from django.urls import path

from . import views as notification_views

urlpatterns = [
     path('' , notification_views.NotificationListView.as_view() , name = 'list_notifications'),
     ]