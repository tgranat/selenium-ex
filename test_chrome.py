import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# This fixture is a generator (using 'yield' instead of 'return').
# The first iteration of the fixture (the webdriver initialization) is the setup phase 
# and is called before the test begins. 
# The second iteration ('quit' call) is the cleanup phase and is called after a test completes


# <input id="search_form_input_homepage" class="js-search-input search__input--adv" type="text" 
# autocomplete="off" name="q" tabindex="1" value="" autocapitalize="off" autocorrect="off">

SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    
def test_search(browser):
    browser.get('http://duckduckgo.com')
    # <link title="DuckDuckGo" type="application/opensearchdescription+xml" rel="search" href="https://duckduckgo.com/opensearch.xml?atb=v194-2__">
    assert(browser.title[:10] == 'DuckDuckGo' )

    # Writing locators as class attribute tuple makes it more flexible than
    # using explicit methods like find_element_by_id, find_element_by_name etc. 
    inputElement = browser.find_element(*SEARCH_INPUT)
    # Search string + return key
    inputElement.send_keys('granat' + Keys.RETURN)
    # Not necessary, we sent a 'return' key:
    #inputElement.submit()
    
    
     
    
