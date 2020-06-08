from django.urls import path
from keramika_ostrovni_web import views

urlpatterns = [
    path("", views.index, name="index"),
    path("deti", views.children, name="children"),
    path("deti-signup", views.children_sign_up, name="children_sign_up"),
    path("deti-login", views.children_login, name="children_login"),
    path("deti-logout", views.children_logout, name="children_logout"),
    path("dospeli", views.adults, name="adults"),
    path("lektori", views.teachers, name="teachers"),
]
