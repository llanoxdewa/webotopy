#!\llano\python\web-scraping-bsoup\.env/Scripts/python

from selenium.webdriver.common.by import By
import unittest
from webotopy.web import WebDriver
from webotopy.page import BasePage, Element 
from time import sleep



@WebDriver.target_url(url='https://www.saucedemo.com/')
class SauceDemo(BasePage):

    def login(self):
        
        username        = self.find(By.ID,'user-name')
        password        = self.find(By.ID,'password')
        login_button    = self.find(By.ID,'login-button')

        username.send_keys('standard_user')
        sleep(2)
        password.send_keys('secret_sauce')
        sleep(2)

        login_button.click()



class Testing(unittest.TestCase):

    def test_just_open_url(self):
        web_page = SauceDemo()

        web_page.run()

        web_page.login()

        sleep(3)


if __name__ == "__main__":
    

    # unittest.TextTestRunner().run(
    #     unittest.TestLoader().loadTestsFromName('main.Main.test_disabled_input')
    # )
    unittest.main()
