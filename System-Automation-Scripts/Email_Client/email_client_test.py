from email_client import EmailClient
import unittest


class EmailClientTest(unittest.TestCase):
    """ Tests for EmailClient class
        """

    # credentials
    # using Google mail server
    __server = 'smtp.gmail.com'
    __port_number = 587
    # sender's credentials
    __username = 'sender@gmail.com'
    with open('password.txt', 'r') as pass_file:
        __password = pass_file.read()
    # recipient's email addr
    __recipient = 'recipient@email.com'

    # test case #1 - testing sending functionality of EmailClient class
    def test_email_client_send(self):
        # Email message content
        # Email subject
        subject = 'Testing'
        # Email body
        body = 'Hi,\n\nI am Kevin. How are you?'
        # Email signature
        signature = '\n\nKind regards,\n{}'.format(self.__username)

        # sending Email
        email_client = EmailClient(
            self.__server, self.__port_number, self.__username, self.__password)
        email_client.set_subject(subject)
        email_client.set_body(body)
        email_client.set_signature(signature)
        email_client.add_attachment('test.txt')

        # testing
        sent = True
        self.assertEqual(email_client.send(self.__recipient), sent)

    # test case #2 - EmailClient Should not send empty emails
    def test_empty_email(self):
        # Empty Email message content
        # Email subject
        subject = ''
        # Email body
        body = ''
        # Email signature
        signature = ''

        # sending Email
        email_client = EmailClient(
            self.__server, self.__port_number, self.__username, self.__password)
        email_client.set_subject(subject)
        email_client.set_body(body)
        email_client.set_signature(signature)

        # testing
        sent = False
        self.assertEqual(email_client.send(self.__recipient), sent)

    # test case #3 - testing reset functionality in EmailClient class
    def test_email_client_reset(self):
        # Email message content
        # Email subject
        subject = 'Testing Reset Method'
        # Email body
        body = 'Email body has not been reset. Please check its functionality.'
        # Email signature
        signature = '\n\nKind regards,\nkevinmanojpatel@gmail.com'

        # initialising Email
        email_client = EmailClient(
            self.__server, self.__port_number, self.__username, self.__password)
        email_client.set_subject(subject)
        email_client.set_body(body)
        email_client.set_signature(signature)
        email_client.add_attachment('test.txt')

        # resetting email content
        email_client.reset_email()

        # adding Email body
        new_body = 'Email body has been reset.'
        email_client.set_body(new_body)

        # testing
        sent = True
        self.assertEqual(email_client.send(self.__recipient), sent)

    # test case #4 - testing sending functionality when special case of attachment added but not subject
    def test_email_client_send_misc(self):
        # Email message content
        # Email subject
        subject = ''

        # sending Email
        email_client = EmailClient(
            self.__server, self.__port_number, self.__username, self.__password)
        email_client.set_subject(subject)
        # add Email attachment
        email_client.add_attachment('test.txt')

        # testing
        sent = False
        self.assertEqual(email_client.send(self.__recipient), sent)


if __name__ == '__main__':
    unittest.main()  # running tests on EmailClient
