from pages.browser import Browser
from selenium import webdriver
from locators import *
import time


class LoginPage(Browser):

    def __init__(self):
        self.LOGIN = '/'

    def log_in_as(self, username, password):
        """
        Locates username & password elements
        and sends credentials and clicks submit 
        """
        self.visit(self.LOGIN)
        username_field = self.find_element(*LoginPageLocators.username_field)
        password_field = self.find_element(*LoginPageLocators.password_field)
        submit_btn = self.find_element(*LoginPageLocators.submit_btn)
        username_field.send_keys(username)
        password_field.send_keys(password)
        submit_btn.click()
        time.sleep(2)

    def get_auth_message(self):
        """
        Locates and verifies
        message after authentication.
        """
        return self.find_element(*LoginPageLocators.message)

    def click_register_link(self):
        """
        Clicks on the "Create an account" link
        """
        create_account_link = self.find_element(*LoginPageLocators.create_acct_link)
        create_account_link.click()
        time.sleep(2)

    def get_page_header(self):
        """
        Returns the CreatePage header
        """
        return self.find_element(*CreateAccountPageLocators.header)