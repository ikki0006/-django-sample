"""middleware module
Example:
    middleware用モジュール
"""
from logging import getLogger
from django.conf import settings
from django.shortcuts import redirect


class LoggingMiddleware:
    "logging用ミドルウェア"
    logger = getLogger("django")

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        self.logger.info(request)
        response = self.get_response(request)
        return response


class AuthCheckMiddleware:
    """認証チェック用のミドルウェア
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 認証対象外ページであればそのままリターンさせる
        if request.path in settings.NON_AUTH_PATH:
            return self.get_response(request)

        # Azure認証情報があればそのままリターンさせる
        if 'user' in request.session:
            if 'preferred_username' in request.session['user']:
                return self.get_response(request)

        # 認証情報がなく、認証対象ページであればsessionに本来の情報を詰めてリダイレクトさせる
        # 本来はvueのurlを貰う必要がある。。。後で変更が必要。。。/login/にパラメータつけてもらうのが良いかも
        request.session['next'] = request.get_full_path()
        return redirect('/general-ui/login/')
