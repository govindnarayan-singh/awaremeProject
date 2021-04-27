from django.urls import path
from . import views

urlpatterns = [
      path('',views.index,name="index"),
      path('details/',views.orgList,name="details"),
      path('profileOrg/<str:pk_value>/',views.org_profile,name="org_profile"),
      path('Createfeed/',views.createFeed,name="feed"),
      path('listFeed/',views.listFeed,name="listFeed"),
      path('newsFeed/<str:pk>/',views.newsFeed,name="newsFeed"),
      path('updateFeed/<str:pk>',views.updateFeed,name="updateFeed"),
      path('deleteFeed/<str:pk>/',views.deleteFeed,name="deleteFeed"),
      path('register/',views.orgRegister,name="register"),
      path('login/',views.user_login,name="login"),
      path('logout/',views.user_logout,name="logout"),    
]