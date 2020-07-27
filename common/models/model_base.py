"""model用共通クラス定義ファイル"""
from django.db import models
from datetime import datetime


class ModelBase(models.Model):
    """model用共通クラス"""
    delete_flg = models.CharField(max_length=1, default='0')
    create_date = models.DateTimeField(default=datetime.now)
    create_user = models.CharField(max_length=20)
    update_date = models.DateTimeField(auto_now=True)
    update_user = models.CharField(max_length=20)

    class Meta:
        abstract = True
