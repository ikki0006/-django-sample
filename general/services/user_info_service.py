"""user_info view module
Example:
    user_info　変換モジュール
"""
from common.utils.response import response
from common.utils.user_info import UserInfo
from general.serializers.user_info_response_serializers import UserInfoSerializer


class UserInfoService:
    """ユーザ情報取得用エンドポイントclass"""

    def get_user_info(self, request):
        """ユーザ情報取得用エンドポイントの関数
        Args:
            request(object): POSTでクライアントより送られてきた情報
        Returns:
           object: Viewに返却するResonse情報
        """

        user_data = UserInfo().get_user_info(request)
        selializer = UserInfoSerializer(user_data)
        return response(response_body=selializer.data)
