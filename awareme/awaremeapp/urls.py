from django.urls import path
from . import views

urlpatterns = [
      path('details/',views.orgList,name="details"),
      path('profileOrg/<str:pk_value>/',views.org_profile,name="org_profile"),
      path('Createfeed/',views.createFeed,name="feed"),
      path('search/',views.search,name="search"),
      path('donation/',views.donating,name="donation"),
      path('listdonated/',views.listdonated,name="listdonate"),
      path('listFeed/',views.listFeed,name="listFeed"),
      path('publishedFeed/',views.refineFeed,name="publishedFeed"),
      path('search/',views.search,name="search"),
      path('newsFeed/<str:pk>/',views.newsFeed,name="newsFeed"),
      path('postComment/<str:pk>/',views.postComment,name="postComment"),
      path('updateFeed/<str:pk>',views.updateFeed,name="updateFeed"),
      path('deleteFeed/<str:pk>/',views.deleteFeed,name="deleteFeed"),
      path('account_setting/',views.account_set,name="account_setting"),
      path('register/',views.orgRegister,name="register"),
      path('mission/',views.mission,name="mission"),
      path('login/',views.user_login,name="login"),
      path('logout/',views.user_logout,name="logout"),    
]