from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_is_successful(self):
        """Test creating a new user with email is successful"""
        email = "bilaltahir3636@gmail.com"
        password = "Pass1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "bilaltahir3636@GMAIL.COM"
        password = "Pass1234"
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with invalid email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "Pass123")

    def test_create_new_super_user(self):
        """Test creating a new super user"""
        email = "bilaltahir3636@gmail.com"
        password = "Pass1234"
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
