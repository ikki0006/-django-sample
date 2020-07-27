"""response module
Example:
    response用モジュール
"""


class LoginResponse(object):
    """R
          Args:
              message(string): Error, dangerの場合に返すメッセージ
              response(dict): response_bodyの中に入れる内容
              https_status(object): restframeworkのstatusモジュールで定義されるhttpステータスオブジェクト

          Returns:
             object: Viewを経由してクライアントに返却するResonse情報
      """

    def __init__(self, redirect_url):
        self.__redirect_url = redirect_url

    @property
    def redirect_url(self):
        """redirect_url getter
          Returns: redirect_urlの返却
        """
        return self.__redirect_url

    @redirect_url.setter
    def redirect_url(self, val):
        self.__redirect_url = val
