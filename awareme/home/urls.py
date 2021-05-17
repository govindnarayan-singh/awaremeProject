from django.urls import path
from home import views


urlpatterns = [
    path('',views.home,name="home"),
    # path('homeorg/',views.homeorg,name="homeorg"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('contact',views.ContactUs,name="contact"),
]
