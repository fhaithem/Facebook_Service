from selenium import webdriver
import time   
import pathlib   
from sys import platform    
    
    
class Selenium:
    def __init__(self):
        """class constructor"""
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        if platform == 'linux':
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.add_argument("--disable-extensions")
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument("--disable-gpu")
            options.add_argument("--allow-insecure-localhost")
            options.add_argument("--verbose")
            options.add_argument("--disable-web-security")
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
            options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36')
            options.binary_location='/usr/bin/google-chrome-stable'
            prefs = {"profile.default_content_setting_values.notifications": 2}

            self.driver = webdriver.Chrome(options=options,
                                            executable_path='/usr/local/bin/chromedriver')
        if platform == 'win32':
            self.driver = webdriver.Chrome(options=options,
                                            executable_path=str(
                                                pathlib.Path().absolute().parent.joinpath('Facebook').joinpath(
                                                    'chromedriver')))
        self.driver.get('https://www.facebook.com/')
        time.sleep(3)
    
    def get_driver(self):
        return self.driver

    def login(self):
        """Login to Facebook account"""
        self.driver.find_element_by_name("email").send_keys('hfrad@kaisensdata.fr')
        self.driver.find_element_by_name("pass").send_keys('Test533007')
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)
        

    def navigate(self, url):
        """navigate to specifique url with selenium"""
        self.driver.get(url)
        time.sleep(3)
        return self.driver

    def scroll(self, c):
        """scroll number of times"""
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", c[len(c) - 1])
        except:
            pass


    def scroll_to_end(self):
        """scroll to the end of the window"""
        SCROLL_PAUSE_TIME = 3

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
    
    def sleep(self, n):
        time.sleep(n)