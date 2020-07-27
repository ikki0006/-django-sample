"""user info response module
    user情報response用モジュール
"""


class UseeInfoResponse(object):
    """Response用汎用関数
          Args:
              user_id(int): DB上ユーザid
              user_name(string): ユーザ名
              user_section(string): 部署名
              user_category_list(list): 各種権限情報
      """

    def __init__(self, user_id, user_name, user_section, user_category_list):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__user_section = user_section
        self.__user_category_list = user_category_list

    @property
    def user_id(self):
        """user_id getter
          Returns: user_idの返却
        """
        return self.__user_id

    @user_id.setter
    def user_id(self, val):
        self.__user_id = val

    @property
    def user_name(self):
        """user_name getter
            Returns: user_nameの返却
        """
        return self.__user_name

    @user_name.setter
    def user_name(self, val):
        self.__user_name = val

    @property
    def user_section(self):
        """user_section getter
            Returns: user_sectionの返却
        """
        return self.__user_section

    @user_section.setter
    def user_section(self, val):
        self.__user_section = val

    @property
    def user_category_list(self):
        """user_category_list getter
          Returns: user_category_listの返却
        """
        return self.__user_category_list

    @user_category_list.setter
    def user_category_list(self, val):
        self.__user_category_list = val
