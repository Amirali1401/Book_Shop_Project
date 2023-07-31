from django.test import TestCase
from django.urls import reverse

from .models import Notification

# Create your tests here.


class NotificationTest(TestCase):

      def test_list_notification_url_by_name(self):
           response = self.client.get(reverse('list_notifications'))
           return self.assertEqual(response.status_code , 302)