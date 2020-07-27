"""sample view module
Example:
    repository層のサンプルモジュール
"""
from sequences import get_next_value
from sample.models import TbTrnSample


class SampleUserRepository():
    """Repositoryのサンプル
    """

    def get_user(self, user_name):
        """user情報を取得

        Args:
            name(str): user名

        Returns:
           list: nameに一致するuserデータを返却
        """
        return TbTrnSample.objects.filter(user_name=user_name)

    def create_user(self, user_name, memo):
        """user情報を登録

        Args:
            name(str): user名
            memo(str): test用メモ

        Returns:
           list: 登録内容を返送
        """
        result = TbTrnSample(user_id=get_next_value('sq_user_id'), user_name=user_name,
                             memo=memo, create_user=user_name, update_user=user_name).save()
        return result
