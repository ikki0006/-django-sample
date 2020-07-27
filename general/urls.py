"""sample urls module
djangoのURLエンドポイント指定用モジュール
"""
from django.urls import path
from general.views import login_view, user_info_view, dummy_login_view

urlpatterns = [
    path('login/', login_view.LoginView.as_view()),
    path('callback/', login_view.CallbackView.as_view()),
    path('user-info/', user_info_view.UserInfoView.as_view()),
    path('dummy-login/', dummy_login_view.DummyLoginView.as_view()),
]
