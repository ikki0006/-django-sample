"""sample view module
Example:
    djangoのrestframeworkで使用されるviewのサンプル

Todo:
    * For module TODOs
    * createの作成。searchの作成

"""

from logging import getLogger
from rest_framework import status, views
from rest_framework.response import Response
from django.db import transaction
from common.utils.logger import trace_logger
from common.utils.response import response
from sample.services.sample_service import SampleService


class SampleSearchView(views.APIView):
    """DB selectのサンプル用エンドポイントclass
    Attributes:
        logger (object): log用attribute. logger.info("message")で使用. infoはerrorなども可
    """
    logger = getLogger(__name__)

    @trace_logger()
    def post(self, request):
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
        service_resp = SampleService().sample_seach(request)
        return Response(service_resp, status.HTTP_200_OK)


class SampleCreateView(views.APIView):
    """DB insertのサンプル用エンドポイントclass
    Attributes:
        logger (object): log用attribute. logger.info("message")で使用. infoはerrorなども可
    """
    logger = getLogger(__name__)

    @trace_logger()
    @transaction.atomic
    def post(self, request):
        """DBのselectをするAPIエンドポイントの関数
        Args:
            request(object): POSTでクライアントより送られてきたHttp情報

        Returns:
           object: クライアントに返却するResonse情報
        """
        service_resp = SampleService().sample_create(request)
        return response(status.HTTP_200_OK, response_body=service_resp)


class SampleGetView(views.APIView):
    """get用のサンプル用エンドポイントclass
    Attributes:
        logger (object): log用attribute. logger.info("message")で使用. infoはerrorなども可
    """
    @trace_logger()
    def get(self, request):
        """GetのテストをするAPIエンドポイントの関数
        Args:
            request(object): Pクライアントより送られてきたHttp情報

        Returns:
           object: クライアントに返却するResonse情報
        """
        body = {'test': "test"}
        return response(response_body=body)
