"""dummy login module
    dummy login用モジュール
"""
from rest_framework import status
from common.utils.response import response
from general.repositories.login_repository import UserRepository
from general.serializers.login_response_serializers import LoginSerializer


class DummyLoginService():
    """Serviceのサンプル
    Attributes:
        属性の名前 (属性の型): 属性の説明
        属性の名前 (:obj:`属性の型`): 属性の説明.
    """

    def dummy_login(self, request):
        """tset用のdummy loginをするAPIエンドポイントの関数
        Args:
            request(object): クライアントより送られてきたHttp情報

        Returns:
           object: Viewを経由してクライアントに返却するResonse情報
        """
        # key確認
        if 'preferred_username'not in request.data:
            return response(http_status=status.HTTP_401_UNAUTHORIZED, message='preferred_usernameがありません')
        # Azure AD 側の oid とアプリ側の external_id が一致するユーザーがいるか確認する
        azure_preferred = request.data['preferred_username']
        user = UserRepository().get_user(azure_preferred)
        if user is None:
            return response(http_status=status.HTTP_401_UNAUTHORIZED, message='DBにユーザが登録されていないか重複しています')

        # sessionに必要情報を詰める
        self._set_session(request, user)

        if not request.session.session_key:
            request.session.save()
        body = {'session_id': request.session.session_key,
                'user_id': request.session['system_cache']['user_id'],
                'user_name': request.session['system_cache']['user_name'],
                'user_section': request.session['system_cache']['user_section'],
                'user_category_list': request.session['system_cache']['user_category_list']
                }

        return response(response_body=body)

    def _set_session(self, request, user):
        """sessionのデータ登録用
        Args:
            cache(object): azure adのAPI scope 基本readのみ

        Returns:
           object: クライアントに返却するResonse情報
        """
        request.session.set_expiry(10800)

        request.session['system_cache'] = {}
        request.session['system_cache']['user_id'] = user.user_id
        request.session['system_cache']['user_name'] = user.user_name
        request.session['system_cache']['user_section'] = user.user_section
        request.session['system_cache']['user_category_list'] = user.user_category_list
        # dummyのみ必要
        request.session['user'] = {}
        request.session['user']['preferred_username'] = request.data['preferred_username']
