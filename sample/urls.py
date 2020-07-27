"""sample urls module
djangoのURLエンドポイント指定用モジュール
"""
from django.urls import path
from sample.views import sample_view

urlpatterns = [
    path('search/', sample_view.SampleSearchView.as_view()),
    path('create/', sample_view.SampleCreateView.as_view()),
    path('get/', sample_view.SampleGetView.as_view()),
]
