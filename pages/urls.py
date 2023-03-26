from django.urls import path

from . import views as pages_views

urlpatterns = [
  path('contactus/' , pages_views.contactus_view , name ='contactus'),
  path('aboutus/' , pages_views.AboutUs.as_view() , name = 'aboutus'),
  ]