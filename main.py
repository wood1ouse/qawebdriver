from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def makeSearchParam(search_str):
    result = ''
    string = search_str.split(" ")
    for word in range(len(string)):
        result += f'{string[word]}+'

    return result


base_url = 'https://www.udemy.com/?persist_locale=&locale=en_US'
input_classname = '[class="udlite-text-input udlite-text-input-large udlite-text-md udlite-search-form-autocomplete-input"]'
heading_classname = '[class="udlite-heading-xxl search--header-title--3wfny"]'

search_term = 'Time Management'

browser = webdriver.Chrome()
browser.get(base_url)

browser.find_element_by_css_selector(input_classname).send_keys(search_term)
browser.find_element_by_css_selector(input_classname).send_keys(Keys.RETURN)

browser.implicitly_wait(10)

browser.get(f'https://www.udemy.com/courses/search/?q={makeSearchParam(search_term)}')

search_result = browser.find_element_by_css_selector(heading_classname).text

actual_result = search_result.split('for ')[1]

assert f'“{search_term.lower()}”' == actual_result



