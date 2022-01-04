from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

User = get_user_model()


class UserAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='michal', email='michal@michal.com')
        user.set_password('123')
        user.save()

    def test_created_user_std(self):
        qs = User.objects.filter(username='michal')
        self.assertEqual(qs.count(), 1)

    def test_created_user_api(self):
        url = api_reverse('api-auth:register')
        data = {
            'username': 'michal123',
            'email': 'michal123@gm.com',
            'password': '123',
            'password2': '123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        token_len = len(response.data.get('token', 0))
        self.assertGreater(token_len, 0)

    def test_login_user_api(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'michal',
            'password': '123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get('token', 0)
        if token:
            token_len = len(token)
        else:
            token_len = 0

        self.assertGreater(token_len, 0)

    def test_login_user_fail_api(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'michal11',
            'password': '123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        token = response.data.get('token', 0)
        if token:
            token_len = len(token)
        else:
            token_len = 0
        self.assertEqual(token_len, 0)

    def test_login_token_api(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'michal',
            'password': '123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get('token', None)
        self.client.credentials(HTTP_AUTHORIZATION='JWT '+token)
        response2 = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)