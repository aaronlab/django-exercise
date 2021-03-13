from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Create a new user with an email is successful"""
        email = 'test@test.test'
        password = 'TestPassword'
        name = 'Test User'

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            name=name
        )

        self.assertEquals(user.email, email)
        self.assertEquals(user.name, name)
        self.assertTrue(user.check_password(password))
