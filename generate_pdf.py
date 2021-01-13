import sys
import json, base64
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait



def execute_command(driver, cmd, params):
    resource = "/session/%s/chromium/send_command_and_get_result" %driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd':cmd, 'params':params})
    response = driver.command_executor._request('POST', url, body)
    if response.get('status'):
        raise Exception('exception thrown ',response.get('value'))
    return response.get('value')

def get_pdf_from_url(url, chrome_driver_path, wait_time = 30, fwd_cookies=None, proxy=None):
    webdriver_options = Options()
    webdriver_options.add_argument('--headless')
    webdriver_options.add_argument('--disable-gpu')
    if proxy:
        webdriver_options.add_argument('--proxy-server=%s', proxy)
    
    driver = webdriver.Chrome(chrome_driver_path, options= webdriver_options)

    if fwd_cookies:
        driver.add_cookies(fwd_cookies)

    driver.get(url)

    print_options = {
        'landscape': True,
        'displayHeaderFooter': True,
        'printBackground': True,
        'preferCSSPageSize': True
    }

    result = execute_command(driver, 'Page.printToPDF', print_options)
    driver.quit()
    return base64.b64decode(result['data'])


    