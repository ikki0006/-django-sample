"""sample view module
Example:
    service層のサンプルモジュール

Todo:
    * For module TODOs
    * createの作成。searchの作成

"""
from sample.serializers.sample_serializer import SampleModelSerializer
from sample.repositories.sample_repository import SampleUserRepository


class SampleService():
    """Serviceのサンプル
    Attributes:
        属性の名前 (属性の型): 属性の説明
        属性の名前 (:obj:`属性の型`): 属性の説明.
    """

    def sample_seach(self, request):
        """DBのselectをするAPIエンドポイントの関数
        Args:
            request(object): POSTでクライアントより送られてきたHttp情報

        Returns:
           object: Viewを経由してクライアントに返却するResonse情報

        Raises:
            例外の名前: 例外の説明 (例 : 引数が指定されていない場合に発生 )

        Note:
            注意事項などを記載

        """
        serializer = SampleModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        return serializer.data

    def sample_create(self, request):
        """DBのinsertをするAPIエンドポイントの関数
        Args:
            request(object): POSTでクライアントより送られてきたHttp情報

        Returns:
           object: クライアントに返却するResonse情報

        Raises:
            例外の名前: 例外の説明 (例 : 引数が指定されていない場合に発生 )

        Note:
            注意事項などを記載

        """
        serializer = SampleModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = SampleUserRepository().create_user(
            serializer.data['user_name'], serializer.data['memo'])
        serializer = SampleModelSerializer(instance=result)
        return serializer.data
