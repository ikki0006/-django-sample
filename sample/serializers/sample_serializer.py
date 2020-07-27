"""sample view module
Example:
    django sirializerのサンプルモジュール

Todo:
    * For module TODOs
    * createの作成。searchの作成

"""
from rest_framework import serializers
from sample.models.sample_model import TbTrnSample


class SampleModelSerializer(serializers.ModelSerializer):
    """Modelsirializerのサンプルclass
    """
    class Meta:
        model = TbTrnSample
        fields = ['user_id', 'user_name', 'memo']
        extra_kwargs = {
            'user_id': {
                'read_only': True
            }
        }
