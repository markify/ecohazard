#Name: Lance
#Description: testing hazard report view, buttons
#Usage: testing hazard report gui for view results
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://csc648team07.herokuapp.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_1(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_id("id_title_text").clear()
        driver.find_element_by_id("id_title_text").send_keys("test")
        driver.find_element_by_id("autocomplete").clear()
        driver.find_element_by_id("autocomplete").send_keys("436 gonzalez drive")
        driver.find_element_by_id("id_zipcode").clear()
        driver.find_element_by_id("id_zipcode").send_keys("94132")
        driver.find_element_by_id("id_location").clear()
        driver.find_element_by_id("id_location").send_keys("san francisco")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_content_text").clear()
        driver.find_element_by_id("id_content_text").send_keys("stuff")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Eco Hazards").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
