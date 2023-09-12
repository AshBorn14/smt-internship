from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login_user,name="login"),
    path('application_form/',views.application_form, name="application_form"),
    path('apply/',views.apply, name="apply"),
    path('status/',views.status, name="status"),
    path('startup_applications/',views.startup_applications, name="startup_applications"),
    path('<uuid:application_id>/application_review/',views.application_review, name="application_review"),
]
