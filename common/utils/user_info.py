"""user_info module
    ユーザ情報取得汎用モジュール
"""
from common.entities.user_info_response import UseeInfoResponse


class UserInfo:
    """ユーザ情報取得用汎用Class"""

    def get_user_info(self, request):
        """ユーザ情報取得用エンドポイントの関数
        Args:
            request(object): POSTでクライアントより送られてきた情報
        Returns:
           object: UerInfo用のentityデータ
        """
        user_id = request.session['system_cache']['user_id']
        user_name = request.session['system_cache']['user_name']
        user_section = request.session['system_cache']['user_section']
        user_category_list = request.session['system_cache']['user_category_list']

        return UseeInfoResponse(
            user_id=user_id, user_name=user_name, user_section=user_section,
            user_category_list=user_category_list)
