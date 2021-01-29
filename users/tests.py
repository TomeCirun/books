from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='vedran', email='vedran@baby.com',
            password='jasamikoj')
        self.assertEqual(user.username, 'vedran')
        self.assertEqual(user.email, 'vedran@baby.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()

        admin_user = User.objects.create_superuser(
            username='cirun',
            email='cirun@live.com',
            password='jasamikoj')
        self.assertEqual(admin_user.username, 'cirun')
        self.assertEqual(admin_user.email, 'cirun@live.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
