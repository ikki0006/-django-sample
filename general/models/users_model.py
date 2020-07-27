"""userデータ系model"""
from django.db import models
from common.models.model_base import ModelBase


class TbMstRole(ModelBase):
    """Task to do."""

    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=20)
    role_desc = models.CharField(max_length=120, null=True)

    class Meta:
        db_table = "tb_mst_role"


class TbMstOrganization(ModelBase):
    """Task to do."""
    org_id = models.IntegerField(primary_key=True)
    org_name = models.CharField(max_length=80, null=True)
    org_hierarchy = models.CharField(max_length=1, null=True)
    upper_org_id = models.IntegerField(null=True)
    org_leader_preferred_username1 = models.CharField(max_length=80, null=True)
    org_leader_preferred_username2 = models.CharField(max_length=80, null=True)

    class Meta:
        db_table = "tb_mst_organization"


class TbMstUser(ModelBase):
    """Task to do."""
    user_id = models.IntegerField(primary_key=True)
    preferred_username = models.CharField(max_length=80)
    user_name_sei = models.CharField(max_length=80, null=True)
    user_name_mei = models.CharField(max_length=80, null=True)
    user_name_kana_sei = models.CharField(max_length=80, null=True)
    user_name_kana_mei = models.CharField(max_length=80, null=True)
    user_name_roman_sei = models.CharField(max_length=256, null=True)
    user_name_roman_mei = models.CharField(max_length=256, null=True)
    mail = models.CharField(max_length=240, null=True)
    tel = models.CharField(max_length=15, null=True)
    last_login_date = models.DateTimeField
    org_id = models.ForeignKey(
        TbMstOrganization, on_delete=models.PROTECT, db_column='org_id')
    role_id = models.ForeignKey(
        TbMstRole, on_delete=models.PROTECT, db_column='role_id')
    retired_flg = models.CharField(max_length=1, default='0')

    class Meta:
        db_table = "tb_mst_user"


class TbMstRoleFunction(ModelBase):
    """Task to do."""
    role_function_id = models.IntegerField(primary_key=True)
    role_id = models.IntegerField()
    # role_id = models.ForeignKey(TbMstRole, on_delete=models.PROTECT)
    function_cd = models.CharField(max_length=50)
    authority_level = models.CharField(max_length=1)

    class Meta:
        db_table = "tb_mst_role_function"
