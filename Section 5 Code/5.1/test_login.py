from selenium import webdriver
from pages.login import LoginPage
import unittest

class LoginTestCase(unittest.TestCase):

    def testUserLogin(self):
        # Happy Path - Login Success
        self.login_page = LoginPage()
        user = 'registeredUser'
        password = '1234'
        self.login_page.log_in_as(user, password)
        welcome_message = self.login_page.get_auth_message()
        self.assertIn('Welcome back', welcome_message.text)
        self.login_page.quit()

    def testLoginFail(self):
        self.login_page = LoginPage()
        unregistered_user = 'otherUser'
        bad_password = 'asdf'
        self.login_page.log_in_as(unregistered_user, bad_password)
        message = self.login_page.get_auth_message()
        self.assertIn('Account not found', message.text)
        self.login_page.click_register_link()
        header = self.login_page.get_page_header()
        self.assertIn('Create an Account', header.text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
