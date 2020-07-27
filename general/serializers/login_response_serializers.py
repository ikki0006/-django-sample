"""login sirialize view module
Example:
    login sirializerのサンプルモジュール
"""
from rest_framework import serializers

# pylint: disable=W0223


class LoginSerializer(serializers.Serializer):
    """user info check用
    """
    redirect_url = serializers.CharField()
