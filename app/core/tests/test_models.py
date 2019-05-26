from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    email = 'mohammad@gmail.com'
    password = '123456789'

    def test_create_user_with_email_successful(self):

        user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password
        )

        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))

    def test_new_user_email_normalized(self):
        email = 'mohammad@GMAIL.COM'
        user = get_user_model().objects.create_user(email, self.password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, self.password)

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            email=self.email,
            password=self.password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_stuff)
