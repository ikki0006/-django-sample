"""sample view module
Example:
    repository層のサンプルモジュール
"""
from general.models import TbMstUser
from general.models import TbMstRoleFunction
from general.entities.user_info_response import UseeInfoResponse


class UserRepository():
    """Repositoryのサンプル
    """

    def get_user(self, azure_preferred):
        """user情報を取得

        Args:
            name(str): user名

        Returns:
           list: nameに一致するuserデータを返却
        """
        user_data = TbMstUser.objects.filter(
            preferred_username=azure_preferred, delete_flg=0
        ).select_related('org_id').values(
            'user_id', 'user_name_sei', 'user_name_mei', 'role_id', 'org_id__org_name'
        )

        if len(user_data) != 1:
            return None

        org_data = TbMstRoleFunction.objects.filter(
            role_id=user_data[0]['role_id']
        ).values('function_cd', 'authority_level')

        return UseeInfoResponse(
            user_id=user_data[0]['user_id'],
            user_name=str(user_data[0]['user_name_sei']) +
            ' ' + str(user_data[0]['user_name_mei']),
            user_section=user_data[0]['org_id__org_name'],
            user_category_list=list(org_data)
        )

 # print(TbMstRole.objects.filter(
        #     tbmstuser__isnull=True).query)

        # q = TbMstUser.objects.filter(preferred_username=azure_preferred).values(
        #     'user_id', 'user_name_sei', 'user_name_mei', 'role_id')

        # q.query.join(
        #     left_join(TbMstUser, TbMstRole, "role_id", "role_id")
        # )
