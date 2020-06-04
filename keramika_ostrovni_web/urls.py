from django.urls import path
from keramika_ostrovni_web import views


urlpatterns = [
    path("",views.index,name="index"),
    path("deti", views.children, name="children"),
    path("dospeli", views.adults, name="adults"),
    path("lektori", views.teachers, name="teachers"),
]
