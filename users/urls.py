from django.urls import path
from users import views


urlpatterns = [
    path("sign-up/", views.RegisterView.as_view(), name="sign_up"),
    path("sign-in/", views.SignInView.as_view(), name="sign_in"),
    path("sign-out/", views.SignOutView.as_view(), name="sign_out"),
    path("activate/<int:user_id>/<str:token>/", views.activate_user, name="activate_account"),
]