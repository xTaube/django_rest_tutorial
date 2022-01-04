from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
from status.models import Status


User = get_user_model()


class StatusAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='michal', email='michal@gm.com')
        user.set_password('123')
        user.save()

        status_obj = Status.objects.create(user=user, content='Hello')

    def test_users(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_statuses(self):
        qs = Status.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_status_create(self):
        auth_url = api_reverse('api-auth:login')
        auth_data = {
            'username': 'michal',
            'password': '123'
        }
        auth_response = self.client.post(auth_url, auth_data, format='json')
        token = auth_response.data.get('token', None)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        url = api_reverse('api-status:list')
        data = {
            'content': "some cool test"
        }
        responnse = self.client.post(url, data, format='json')

        # self.assertEqual(responnse.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Status.objects.all().count(), 2)
