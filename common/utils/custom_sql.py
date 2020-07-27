"""SQL直投入用関数"""

from django.db import connection


def custom_sql(sql, bind_params=None):
    """SQL直投入用関数

        Args: 
            sql(string): SQLのクエリ文
            bind_params(dict): SQL文のパラメータ

        Returns:
           list: SQL実行結果。2重list。dictではないので注意
        """
    with connection.cursor() as cursor:
        cursor.execute(sql, bind_params)
        row = cursor.fetchall()
    return row
