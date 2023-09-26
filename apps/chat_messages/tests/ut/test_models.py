from django.test import TestCase
from apps.chat_messages import models

class MessageTestCase(TestCase):
    def setUp(self):
        # Create a sample Message object for testing
        self.message = models.Message.objects.create(username="testuser")


    def test_user_creation(self):
        self.assertEqual(self.message.username,'testuser')
        
    def test_message_str(self):
        # Test the __str__ method of the Message model
        self.assertEqual(str(self.message), "testuser")
        
    def test_verbose_name_plural(self):
        # test verbose_name_plural attribute of models's meta class
        self.assertEqual(models.Message._meta.verbose_name_plural , 'Message')

    def test_username_max_length(self):
        # Test the max_length attribute of the username field
        username_field = models.Message._meta.get_field("username")
        self.assertEqual(username_field.max_length, 50)