"""user info sirialize view module
Example:
    user info sirializerのサンプルモジュール
"""
from rest_framework import serializers

# pylint: disable=W0223


class UserCategorySerializer(serializers.Serializer):
    """user info category listcheck用
    """
    function_cd = serializers.CharField(max_length=10)
    authority_level = serializers.IntegerField()


class UserCategoryListSerializer(serializers.ListSerializer):
    """user info category listcheck用
    """
    child = UserCategorySerializer()


class UserInfoSerializer(serializers.Serializer):
    """user info check用
    """
    user_id = serializers.IntegerField()
    user_name = serializers.CharField()
    user_section = serializers.CharField()
    user_category_list = UserCategoryListSerializer()
