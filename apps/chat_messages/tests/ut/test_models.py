from django.test import TestCase
from apps.chat_messages.models import Message
from apps.chat_users.models import User

class MessageTestCase(TestCase):
    def setUp(self):
        # Create a sample Message object for testing
        self.user1 = User.objects.create_user(
            username='user1',
            password='user1pass',
            first_name='user',
            last_name='one',
            email='user1@test.com',
            title='Python dev',
            bio='Testing stuff'
        )
        
        self.user2 = User.objects.create_user(
            username='user2',
            password='user2pass',
            first_name='user',
            last_name='two',
            email='user2@test.com',
            title='Python dev',
            bio='Testing stuff'
        )
        
        self.message = Message.objects.create(
            sending_user = self.user1,
            receiving_user = self.user2,
            message_body = 'This is a message'
        )


    # def test_user_creation(self):
    #     self.assertEqual(self.message.username,'testuser')
        
    def test_message_str(self):
        
        # Test the __str__ method of the Message model
        expected_str="from user1 to user2"
        self.assertEqual(str(self.message), expected_str)
        
        
    def test_message_match(self):
        self.assertEqual(self.message.message_body, 'This is a message')
        
    def test_verbose_name_plural(self):
        # test verbose_name_plural attribute of models's meta class
        #print(models.Message._meta.verbose_name_plural)
        self.assertEqual(Message._meta.verbose_name_plural , 'Messages')

    # def test_username_max_length(self):
    #     # Test the max_length attribute of the username field
    #     username_field = models.Message._meta.get_field("sending_user")
    #     self.assertEqual(username_field.max_length, 50)