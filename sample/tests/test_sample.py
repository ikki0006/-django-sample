from rest_framework.test import APITestCase, APIRequestFactory
from general.views.dummy_login_view import DummyLoginView
from sample.views.sample_view import SampleGetView

# Create your tests here.


class TestSampleGet(APITestCase):
    """/sample-ui/get/のテスト"""
    TARGET_URL = '/sample-ui/get/'
    DUMMY_USER = 'Azure ADに登録したユーザ'

    def setUp(self):
        # dummy sessionの作成
        # dummy loginによるsessionの作成
        self.client.post('/general-ui/dummy-login/',
                         {'preferred_username': self.DUMMY_USER},
                         format='json')

    def tearDown(self):
        pass

    def test_sample_get(self):
        response = self.client.get(self.TARGET_URL)
        self.assertEqual(response.status_code, 200)
        response_body = {'message': None, 'response_body': {'test': 'test'}}
        self.assertJSONEqual(response.content, response_body)
