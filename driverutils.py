from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class ChromeBot:
    def __init__(self):
        self.driver = self._setup_driver()

    @staticmethod
    def _setup_driver():
        print('Loading...')
        chrome_options = Options()
        chrome_options.add_argument("disable-infobars")
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def _get_element(self, xpath, attempts=5, _count=0):
        '''Safe get_element method with multiple attempts'''
        try:
            element = self.driver.find_element_by_xpath(xpath)
            return element
        except Exception as e:
            if _count<attempts:
                sleep(1)
                print(f'Attempt {_count}')
                self._get_element(xpath, attempts=attempts, _count=_count+1)
            else:
                print("Element not found, raising error")

    def click(self, xpath):
        el = self._get_element(xpath)
        el.click()

    def send_keys(self, xpath, message):
        el = self._get_element(xpath)
        el.click()
        el.send_keys(message)
