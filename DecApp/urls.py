from django.urls import path

from DecApp import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('loginpage', views.loginpage, name="loginpage"),
    path('userpage', views.userpage, name="userpage"),
    path('add_details', views.add_details, name="add_details"),
    path('view_details', views.view_details, name="view_details"),
    path('logout_view', views.logout_view, name="logout_view"),
    path('download-row-pdf/<int:work_number>/', views.download_bill, name='download_row_pdf'),
]
