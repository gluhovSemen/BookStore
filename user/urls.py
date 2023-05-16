from django.urls import path
from user.views import ClientRegistration, ClientLogin, UserLogout

urlpatterns = [
    path("register/", ClientRegistration.as_view(), name="register"),
    path("login/", ClientLogin.as_view(), name="login"),
    path("logout/", UserLogout.as_view(), name="logout"),
]
