import requests
import traceback
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

"""
Front-end tests for the Fibonacci web app
"""

def test_html(url):
    """
    Basic non-Selenium test to make sure expected HTML
    components are on the page.
    """
    r = requests.get(url, timeout=30)
    html = bs(r.content, 'html.parser')
    assert html.title.text == 'Fibonacci Numbers Calculator'
    assert html.h1.text == 'Get Fibonacci number'
    form_input = html.input
    assert form_input
    assert form_input['id'] == 'number'
    button = form_input.button
    assert button['id'] == 'getFibNumber'

def test_submit_valid_number(url):
    """
    Example test using Selenium to submit an HTML form.
    This assumes Firefox is installed.  Asserts will be
    skipped if Firefox cannot be found.
    """
    try:
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10)
        driver.get(url)
        input_field = driver.find_element_by_id('number')
        button = driver.find_element_by_id('getFibNumber')
        input_field.send_keys('4')
        button.click()
        try:
            wait.until(ec.text_to_be_present_in_element_value((By.ID,'number'),'3'))
        except TimeoutException:
            # Expected response not found, continue with assert
            traceback.print_exc()
        assert input_field.get_attribute('value') == '3'
    except OSError as e:
        #Firefox not installed, skip test
        print "Skipping Selenium test, Firefox not installed/found"
    finally:
        if driver:
            driver.quit()

def test_submit_invalid_number(url):
    """
    Example test using Selenium to submit an HTML form.
    Assumption is that the result will display an error
    if invalid input is submitted.
    """
    try:
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10)
        driver.get(url)
        input_field = driver.find_element_by_id('number')
        button = driver.find_element_by_id('getFibNumber')
        invalid_number = 'Hello world!'
        input_field.send_keys(invalid_number)
        button.click()
        try:
            wait.until(ec.text_to_be_present_in_element_value(
            (By.ID,'number'),'Invalid number'))
        except TimeoutException:
            # Expected response not found, continue with assert
            traceback.print_exc()
        result = input_field.get_attribute('value')
        assert result != invalid_number, 'No error message was displayed for invalid input'
    except OSError as e:
        #Firefox not installed, skip test
        print "Skipping Selenium test, Firefox not installed/found"
    finally:
        if driver:
            driver.quit()
