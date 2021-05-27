import unittest
from selenium import webdriver
#from PageObjectModel.locators import ComputerLocators
#from PageObjectModel.page import MainPage
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from PageObjectModel.page import MainPage
from PageObjectModel.locators import MainPageLocators


class FilterComputers(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver.get("http://computer-database.herokuapp.com/computers")
        self.addCleanup(self.driver.quit)

    def testFilterComputer(self):
        self.driver.get('http://computer-database.herokuapp.com/computers/')
        
        #self.assertIn('Computers database', self.browser.title)
        
        SearchSubmitButton = MainPageLocators.SearchSubmitButton
        SearchBox = MainPageLocators.SearchBox
        SearchBox.send_keys('ASCI')
        MainPage.click_filter_button(SearchSubmitButton)
        AlertMessage = MainPageLocators.AlertMessage
        assert text_to_be_present_in_element(AlertMessage, 'Computers found')

        '''
        main_page = page.MainPage(self)
        main_page.search_computer = "ASCIasjsjsjs"
        main_page.click_filter_button()
        search_results_page = page.SearchResultsPage(self.driver)
        assert search_results_page.is_results_found(), 'Nothing to display'
        '''
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()