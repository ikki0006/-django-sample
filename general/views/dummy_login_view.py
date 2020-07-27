"""dummy_login view module
    unit test用ダミーログイン
"""

from rest_framework import status, views
from rest_framework.response import Response
from common.utils.logger import trace_logger
from common.utils.response import response
from general.services.dummy_login_service import DummyLoginService


class DummyLoginView(views.APIView):
    """d用エンドポイントclass
    Attributes:
        logger (object): log用attribute. logger.info("message")で使用. infoはerrorなども可
    """
    @trace_logger()
    def post(self, request):
        """GetのテストをするAPIエンドポイントの関数
        Args:
            request(object): Pクライアントより送られてきたHttp情報

        Returns:
           object: クライアントに返却するResonse情報
        """

        return DummyLoginService().dummy_login(request)
