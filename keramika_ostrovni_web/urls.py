from django.urls import path
from keramika_ostrovni_web import views

urlpatterns = [
    path("", views.index, name="index"),
    path("deti", views.children, name="children"),
    path("account-signup", views.children_sign_up, name="children_sign_up"),
    path("account-login", views.children_login, name="children_login"),
    path("account-logout", views.children_logout, name="children_logout"),
    path("account-info", views.account_info, name="account_info"),
    path("account-info-edit", views.account_info_edit, name="account_info_edit"),
    path("dite-edit/<int:child_id>", views.child_edit, name="child_edit"),
    path("dite-nove", views.child_add_new, name="child_add_new"),
    path("zapis-krouzku", views.children_sign_into_classes, name="children_sign_into_classes"),
    path("zapis-krouzku/zapsano", views.sign_up_child, name="sign_up_child"),
    path("dospeli", views.adults, name="adults"),
    path("dospely-edit/<int:adult_id>", views.adult_edit, name="adult_edit"),
    path("dospely-novy", views.adult_add_new, name="adult_add_new"),
    path("lektori", views.teachers, name="teachers"),
]
