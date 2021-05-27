from PageObjectModel.element import BasePageElement
from PageObjectModel.locators import MainPageLocators, ComputerLocators



class SearchComputer(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    SearchBox = 'Filter by computer name...'


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

        

class MainPage(BasePage):
    """Home page action methods come here. """

    #Declares a variable that will contain the retrieved text
    search_computer = SearchComputer()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Computers database" appears in page title"""

        return "Computers database" in self.driver.title

    def click_button(self):
        """Triggers the add of a computer"""

        element = self.driver.find_element(*MainPageLocators.SearchSubmitButton)
        element.click

        element = self.driver.find_element(*ComputerLocators.AddComputerButton)
        element.click
        
        element = self.driver.find_element(*ComputerLocators.DeleteComputer)
        element.click

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source