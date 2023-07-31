from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notification  ,Question ,Answer

# Create your views here.


class NotificationListView( LoginRequiredMixin,generic.ListView):
    model = Notification
    context_object_name = 'notifications'
    template_name = 'notification/list_notifications.html'

    def get_queryset(self):
        return Notification.objects.filter(user = self.request.user).order_by('id')





