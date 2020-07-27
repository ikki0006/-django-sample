"""sample view module
Example:
    service層のサンプルモジュール

Todo:
    * For module TODOs
    * login時に元々行きたかったページにリダイレクト機能をつける。sessionにnextをもたせる

"""
import uuid
import msal
from django.conf import settings
from rest_framework import status
from django.shortcuts import redirect
from common.utils.response import response
from general.repositories.login_repository import UserRepository
from general.serializers.login_response_serializers import LoginSerializer
from general.entities.login_response import LoginResponse


class LoginService():
    """Serviceのサンプル
    Attributes:
        属性の名前 (属性の型): 属性の説明
        属性の名前 (:obj:`属性の型`): 属性の説明.
    """

    def pre_login(self, request):
        """DBのselectをするAPIエンドポイントの関数
        Args:
            request(object): クライアントより送られてきたHttp情報

        Returns:
           object: Viewを経由してクライアントに返却するResonse情報
        """
        if 'state' not in request.session:
            request.session['state'] = str(uuid.uuid4())
        auth_url = self._build_auth_url(
            scopes=settings.SCOPES, state=request.session['state'])

        selializer = LoginSerializer(LoginResponse(auth_url))
        return response(response_body=selializer.data)

    def after_login(self, request):
        """Azure ad でリダイレクトで戻ってくるエンドポイント用service
        Args:
            request(object): クライアントより送られてきたHttp情報

        Returns:
           object: クライアントに返却するResonse情報
        """
        if request.GET.get('state') != request.session.get('state'):
            # 'state' がリクエスト時と一致しない
            return redirect('https://' + settings.DOMAIN + '/')
        if 'error' in request.GET:
            # Azure AD が認証/認可エラーを返した
            return response(http_status=status.HTTP_401_UNAUTHORIZED, message='Azure Adで認証エラーが発生しました')
        if 'code' in request.GET:
            cache = self._load_cache(request)
            result = self._build_msal_app(cache=cache).acquire_token_by_authorization_code(
                request.GET['code'],
                scopes=settings.SCOPES,  # Misspelled scope would cause an HTTP 400 error here
                redirect_uri=settings.REDIRECT_PATH)
            if 'error' in result:
                return response(http_status=status.HTTP_401_UNAUTHORIZED, message='Azureとの認証確認でエラーが発生しました', )
            request.session['user'] = result.get('id_token_claims')

        # Azure AD 側の oid とアプリ側の external_id が一致するユーザーがいるか確認する
        azure_preferred = request.session['user']['preferred_username']
        user = UserRepository().get_user(azure_preferred)
        if user is None:
            return response(http_status=status.HTTP_401_UNAUTHORIZED, message='DBにユーザが登録されていないか重複しています')

        # sessionに必要情報を詰める
        self._set_session(request, user)

        # pathがあればリダイレクト
        path = 'https://' + settings.DOMAIN + '/'
        if 'next' in request.session:
            path = 'https://' + settings.DOMAIN + request.session['next']

        return redirect('https://' + settings.DOMAIN + '/')

    def _build_auth_url(self, authority=None, scopes=None, state=None):
        """azure ad の認証エンドポイントURL作成用の関数
        Args:
            authority(str): AzureのアプリケーションIDのURL
            scopes(object): azure adのAPI scope 基本readのみ
            state(object):　リダイレクト時の確認のために取得されたuuid

        Returns:
           object: クライアントに返却するリダイレクトurl情報
        """
        return self._build_msal_app(authority=authority).get_authorization_request_url(
            scopes or [],
            state=state or str(uuid.uuid4()),
            redirect_uri=settings.REDIRECT_PATH)

    def _build_msal_app(self, authority=None, cache=None):
        """azure ad の認証エンドポイント用データ作成
        Args:
            cache(object): azure adのAPI scope 基本readのみ

        Returns:
           object: クライアントに返却するResonse情報
        """
        return msal.ConfidentialClientApplication(
            settings.CLIENT_ID, authority=settings.AUTHORITY,
            client_credential=settings.CLIENT_SECRET, token_cache=cache)

    def _load_cache(self, request):
        """azure ad の認証エンドポイント用データ作成
        Args:
            cache(object): azure adのAPI scope 基本readのみ

        Returns:
           object: クライアントに返却するResonse情報
        """
        cache = msal.SerializableTokenCache()
        if request.session.get('token_cache'):
            cache.deserialize(request.session['token_cache'])
        return cache

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
