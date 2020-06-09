from django.urls import path
from keramika_ostrovni_web import views

urlpatterns = [
    path("", views.index, name="index"),
    path("deti", views.children, name="children"),
    path("account-signup", views.children_sign_up, name="children_sign_up"),
    path("account-login", views.children_login, name="children_login"),
    path("account-logout", views.children_logout, name="children_logout"),
    path("dospeli", views.adults, name="adults"),
    path("lektori", views.teachers, name="teachers"),
]
