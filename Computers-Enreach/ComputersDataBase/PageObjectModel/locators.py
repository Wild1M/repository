from selenium.webdriver.common.by import By

class MainPageLocators(object):

    SearchSubmitButton = (By.ID, 'searchsubmit')
    SearchBox = (By.ID, 'searchbox')
    AddNewComputerButton = (By.ID, 'add')
    AlertMessage = (By.CLASS_NAME,'alert-message')
    
class ComputerLocators(object):
    ComputerName = (By.ID, 'name')
    AddComputerButton = (By.CLASS_NAME, 'primary')
    IntroducedDate = (By.ID, 'introduced')
    DiscontinuedDate = (By.ID, 'discontinued')
    CompanyName = (By.ID, 'company')
    DeleteComputer = (By.CLASS_NAME, 'danger')