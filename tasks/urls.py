from django.urls import path
from .views import home, login_view, register_view, tasks_view

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("tasks/", tasks_view, name="tasks"),
]
