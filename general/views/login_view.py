"""login view module
Example:
    Azure ADを使用したlogin用module

"""
from logging import getLogger
from rest_framework import views
from rest_framework.response import Response
from django.db import transaction
from django.shortcuts import redirect
from common.utils.logger import trace_logger
from general.services.login_service import LoginService


class LoginView(views.APIView):
    """DB selectのサンプル用エンドポイントclass
    Attributes:
        logger (object): log用attribute. logger.info("message")で使用. infoはerrorなども可
    """
    logger = getLogger(__name__)

    @trace_logger()
    def get(self, request):
        """DBのselectをするAPIエンドポイントの関数
        Args:
            request(object): POSTでクライアントより送られてきたHttp情報

        Returns:
           object: クライアントに返却するResonse情報

        Raises:
            例外の名前: 例外の説明 (例 : 引数が指定されていない場合に発生 )

        Note:
            注意事項などを記載

        """
        redirect_url = LoginService().pre_login(request)
        return redirect_url


class CallbackView(views.APIView):
    """DB insertのサンプル用エンドポイントclass
    Attributes:
        logger (object): log用attribute. logger.info("message")で使用. infoはerrorなども可
    """
    logger = getLogger(__name__)

    @ trace_logger()
    @ transaction.atomic
    def get(self, request):
        """DBのselectをするAPIエンドポイントの関数
        Args:
            request(object): POSTでクライアントより送られてきたHttp情報

        Returns:
           object: クライアントに返却するResonse情報
        """
        service_resp = LoginService().after_login(request)
        return service_resp
