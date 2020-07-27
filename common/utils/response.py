"""response module
Example:
    response用モジュール
"""
from rest_framework import status
from rest_framework.response import Response


def response(http_status=status.HTTP_200_OK, response_body=None, message=None):
    """Response用汎用関数
        Args:
            message(string): Error, dangerの場合に返すメッセージ
            response(dict): response_bodyの中に入れる内容
            https_status(object): restframeworkのstatusモジュールで定義されるhttpステータスオブジェクト

        Returns:
           object: Viewを経由してクライアントに返却するResonse情報
    """
    return_response = {}
    return_response["message"] = message
    return_response["response_body"] = response_body
    return Response(return_response, http_status)
