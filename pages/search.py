from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:
    URL = 'https://www.duckduckgo.com'
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    
    def __init__(self, browser):
        self.browser = browser
    
    def load(self):
        self.browser.get(self.URL)
        
    def get_title(self):
        return self.browser.title
    
    def search(self, phrase):
        # Writing locators as class attribute tuple makes it more flexible than
        # using explicit methods like find_element_by_id, find_element_by_name etc. 
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
