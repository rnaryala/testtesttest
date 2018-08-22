import math
import unittest
import xmlrunner
from ddt import ddt, file_data
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from main_page import MainPage


@ddt
class TestStringMethods(unittest.TestCase):
    page = None

    def setUp(self):
        options = Options()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        self.page = MainPage(self.driver)
        self.page.open("https://google.ru/")

    def test_title(self):
        title = self.driver.title
        self.assertEqual(title, 'Google')

    def test_button_value(self):
        button = self.page.search_form.get_button_name()
        self.assertEqual(button, 'Google Search')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
    
    @file_data('test_sqrt_data.json')
    def test_sqrt(self, value, result):
        print(result)
        self.assertEqual(math.sqrt(value), result)
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='reports'))
