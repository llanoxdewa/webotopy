#!\llano\python\web-scraping-bsoup\.env/Scripts/python

import unittest
from webotopy.web import WebDriver
from webotopy.page import BasePage, Element 
from time import sleep



@WebDriver.target_url(url='https://www.freepik.com/')
class FreePik(BasePage):
    pass

class Testing(unittest.TestCase):

    def test_just_open_url(self):
        web_page = FreePik()
        web_page.run()



if __name__ == "__main__":
    

    # unittest.TextTestRunner().run(
    #     unittest.TestLoader().loadTestsFromName('main.Main.test_disabled_input')
    # )
    unittest.main()
