from django.urls import path
from . import views 

urlpatterns =[
    path('',views.mainpage),
    path('login',views.login),
    path('signup',views.signup),
    path('logout',views.logout),
    path('Homepage',views.Homepage),
    path('submit_request',views.submit_request),
    path('manage-requests', views.manage_requests),

]