from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.HomePage,name='home'),
    path('signup',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('modelform/',views.modelform,name='modelform'),
    path('ImageModelForm/',views.ImageModelForm,name='imagemodelform'),
    path('showdata/',views.Showdata,name='showdata'),
    path('complete/<int:eno>/', views.complete, name='completeurl'),
    path('userregister/<int:eno>',views.userregister,name='userregistrationform'),
    path('showuser/',views.showusers,name='showusersurl'),
    path('delete/<int:eno>',views.deleteData , name='deleteurl'),
    path('pglogin/',views.pglogin,name='pgloginurl'),
    path('pgsignuppage/',views.pgsignuppage,name='pgsignupurl'),
    path('pglogout',views.pglogout,name='pglogouturl'),
]