
from django.urls import path, include
from .views import (
    UserRegistrationView, 
    UserLoginView, 
    SendOtpView,
    VerifyOtpView,
    ResetPasswordView,
    UpadateProfileView,
    UserProfileView,
    UserLogoutView
)

urlpatterns = [
    path("user-registration", 
        UserRegistrationView.as_view(), 
        name="user-registration"
    ),
    path("user-login", 
        UserLoginView.as_view(),
        name="user-login"
    ),
    path("send-otp",
        SendOtpView.as_view(),
        name="send-otp"
    ),
    path("verify-otp",
        VerifyOtpView.as_view(),
        name="verify-otp"
    ),
    path("reset-password",
        ResetPasswordView.as_view(),
        name="reset-password"
    ),
    path("update-profile",
        UpadateProfileView.as_view(),
        name="update-profile"
    ),
    path("user-profile",
        UserProfileView.as_view(),
        name="user-profile"
    ),
    path("logout",
        UserLogoutView.as_view(),
        name="logout"
    )
]
