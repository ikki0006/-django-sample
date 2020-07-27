"""user_info view module
Example:
    user情報の返信モジュール
"""
from rest_framework import views
from common.utils.logger import trace_logger
from general.services.user_info_service import UserInfoService


class UserInfoView(views.APIView):
    """user情報用エンドポイントclass
      Attributes:
          logger (object): log用attribute. logger.info("message")で使用. infoはerrorなども可
    """
    @trace_logger()
    def post(self, request):
        """user情報を提供するAPIエンドポイントの関数
        Args:
            request(object): POSTでクライアントより送られてきた情報
        Returns:
           object: クライアントに返却するResonse情報
        """

        return UserInfoService().get_user_info(request)
