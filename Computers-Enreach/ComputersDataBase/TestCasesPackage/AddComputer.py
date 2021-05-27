from selenium import webdriver
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
import unittest
from PageObjectModel.locators import ComputerLocators


class AddComputers(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        #self.driver.get("http://computer-database.herokuapp.com/computers")
        self.addCleanup(self.browser.quit)

    def testAddComputer(self):
        self.browser.get('http://computer-database.herokuapp.com/computers/new')
        self.assertIn('Computers database', self.browser.title)
        
        #ComputerName = MainPage(self.driver)
        ComputerName = ComputerLocators.ComputerName
        ComputerName.send_keys('MartinPC')
        AddComputer = ComputerLocators.AddComputerButton
        AddComputer.click()
        #validators.url('http://computer-database.herokuapp.com/computers')
        alertmessage = self.browser.find_element_by_class_name('alert-message')        
        #if alertmessage.contains('Done!')
        assert text_to_be_present_in_element(alertmessage, 'Done!')
        #text_to_be_present_in_element(alertmessage, 'Done!')         


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()