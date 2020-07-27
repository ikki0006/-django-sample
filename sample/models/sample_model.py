"""説明を記載"""
from django.db import models
from common.models.model_base import ModelBase


class TbTrnSample(ModelBase):
    """Task to do."""
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=10)
    memo = models.CharField(max_length=200)

    class Meta:
        db_table = "tb_trn_sample"
