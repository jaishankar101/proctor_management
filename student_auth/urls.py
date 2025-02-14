from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('signin/student/',views.student_signin , name='student_signin'),
    path('signup/student/', views.student_signup , name='student_signup'),
    path('signout', views.signout , name='signout'),
    path('activate/<uidb64>/<token>',views.activate, name='activate'),
    path("forgotPassword", views.forgotPassword,name="forgotPassword"),
    path('resetPassword/<uidb64>/<token>',views.resetPassword,name="resetPassword"),
    path("resetPassword/done/",auth_views.PasswordResetDoneView.as_view(template_name="authentication/password/password_reset_done.html"),name="password_reset_done",),
    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(template_name="authentication/password/password_reset_complete.html"),name="password_reset_complete",),
]
