from django.urls import path
from users import views


urlpatterns = [
    path("sign-up/", views.register, name="sign_up"),
    path("sign-in/", views.sign_in, name="sign_in"),
    path("sign-out/", views.sign_out, name="sign_out"),
    path("activate/<int:user_id>/<str:token>/", views.activate_user, name="activate_account"),
]