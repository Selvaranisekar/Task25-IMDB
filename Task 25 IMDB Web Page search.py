import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class imdb:

    def __init__ (self,url):

        self.url=url
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        WebDriverWait(self.driver, 30)
        print("Login success")

    def search_title_name(self):

        self.driver.execute_script("window.scrollBy(0,500)","")
        Title_name=self.driver.find_element(By.XPATH,"//label[@for='accordion-item-titleNameAccordion']")
        time.sleep(5)
        Title_name.click()
        action=ActionChains(self.driver)
        a = self.driver.find_element(By.XPATH, "(//div[@role='presentation'])[34]")
        action.key_down(Keys.CONTROL).click(a).key_up(Keys.CONTROL).send_keys("CaptainMiller").perform()
        see_results=self.driver.find_element(By.XPATH,"//button[@aria-label='See results']")
        action.double_click(see_results).perform()
        print("Title name:search Done")
        print("URL:",self.driver.current_url)


if __name__=="__main__":
    im=imdb("https://www.imdb.com/search/title/")
    im.start()
    im.search_title_name()

