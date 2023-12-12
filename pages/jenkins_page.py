import logging
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
logging.basicConfig(level=logging.INFO)


class JenkinsPage:
    def __init__(self, driver):
        self.driver = driver
        self.input_name_locator = (By.XPATH, '//*[@id="j_username"]')
        self.input_password_locator = (By.XPATH, '//*[@id="j_password"]')
        self.enter_website_button = (By.XPATH, '//*[@id="root"]/div/main/div/div/section[1]/div/footer/button')
        self.last_build_locator = (By.XPATH, '//*[@id="pipeline-box"]/div/div/table/tbody[2]/tr[1]')
        self.agent1_time_locator = (By.XPATH, '//*[@id="pipeline-box"]/div/div/table/tbody[2]/tr[1]/td[5]/div/div/div[1]/span')
        self.agent2_time_locator = (By.XPATH, '//*[@id="pipeline-box"]/div/div/table/tbody[2]/tr[1]/td[6]/div/div/div[1]/span')
        self.agent3_time_locator = (By.XPATH, '//*[@id="pipeline-box"]/div/div/table/tbody[2]/tr[1]/td[7]/div/div/div[1]/span')
        self.report_link_locator = (By.XPATH, '//*[@id="buildHistory"]/div[2]/table/tbody/tr[2]/td/div[1]/div[2]/div/a')


    def enter_credentials(self):
        input_name = self.driver.find_element(*self.input_name_locator)
        input_pwd = self.driver.find_element(*self.input_password_locator)
        input_name.send_keys("Yaroslav")
        input_pwd.send_keys("124Pan673")
        input_pwd.send_keys(Keys.ENTER)

    def confirm_entering_website(self):
        button = self.driver.find_element(*self.enter_website_button)
        button.click()

    def classes(self):
        return self.build_failed()

    def build_failed(self):
        build = self.driver.find_element(*self.last_build_locator)
        stages = build.find_elements(By.XPATH, "./*")[:2]
        for stage in stages:
            if "FAILED" in stage.get_attribute("class"):
                return True
        return False

    def count_time_taken(self):
        time1 = int(self.driver.find_element(*self.agent1_time_locator).text[0])
        time2 = int(self.driver.find_element(*self.agent2_time_locator).text[0])
        time3 = int(self.driver.find_element(*self.agent3_time_locator).text[0])
        return max(time1, time2, time3)

    def report_link_exists(self):
        try:
            self.driver.find_element(*self.report_link_locator)
            return True
        except:
            return False
