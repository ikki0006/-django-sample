"""common logger module
共通log出力モジュール

ToDo:
 errハンドリング時にwebAppExpectionからresponseが返るようにする
"""
from functools import wraps
from logging import getLogger
from time import time
from rest_framework import status
from common.utils.exception import WebAppException
from common.utils.response import response


def trace_logger():
    """デコレーターでloggerを引数にとるためのラッパー関数
    Args:
        logger (logging.Logger)
    Returns:
        _decoratorの返り値
    """

    def _decorator(func):
        """デコレーターを使用する関数を引数とする
        Args:
            func (function)
        Returns:
            wrapperの返り値
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            """実際の処理を書くための関数
            Args:
                *args, **kwargs: funcの引数
            Returns:
                funcの返り値
            """
            logger = getLogger("django")

            # sessionの中にユーザ情報があればユーザ名を取得
            try:
                user = args[1].session['user']['preferred_username']
            except (AttributeError, KeyError):
                user = 'Anonymous User'
            post_data = args[1].data
            logger.info("%s module start", str(args[0].__class__))
            logger.info("%s post_data user: \"%s\" body: %s",
                        str(args[0].__class__), user, post_data)
            start_time = time()
            try:
                result = func(*args, **kwargs)
            except WebAppException as err:
                # funcのエラーハンドリング
                elapsed_time = time() - start_time
                logger.error(err, exc_info=True)
                logger.error("%s module killed -> elapsed time: %ss",
                             str(args[0].__class__), elapsed_time)
                response(status.HTTP_500_INTERNAL_SERVER_ERROR, message='内部エラー')
            else:
                elapsed_time = time() - start_time
                logger.info("%s module completed -> elapsed time: %ss",
                            str(args[0].__class__), elapsed_time)
            return result
        return wrapper
    return _decorator
