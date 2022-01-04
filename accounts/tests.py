from django.test import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='michal', email='michal@michal.com')
        user.set_password('123')
        user.save()

    def test_created_user(self):
        qs = User.objects.filter(username='michal')
        self.assertEqual(qs.count(), 1)
