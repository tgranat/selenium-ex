import pytest
from selenium.webdriver import Chrome

from pages.search import DuckDuckGoSearchPage

@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    
def test_search(browser):
    PHRASE = 'pytest selenium'
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    # Assert title is correct
    assert(search_page.get_title()[:10] == 'DuckDuckGo')
    search_page.search(PHRASE)
    # Assert title now starts with search phrase (search has been successful)
    assert(search_page.get_title()[:len(PHRASE)] == PHRASE)
    
     
    
