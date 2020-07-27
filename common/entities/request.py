""" bat request entity
    bat用requestデータ保持entity
"""


class BatRequest(object):
    """Request用汎用class
         Args:
             data(dict): requestデータ
     """

    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        """data getter
          Returns: dataの返却
        """
        return self.__data

    @data.setter
    def data(self, val):
        self.__data = val
