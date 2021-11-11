from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from .element import BasePageElement
from .locators import MainPageLocators

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver:WebDriver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return "Iterograph" in self.driver.title

    def open_layer_panel(self):
        element = self.driver.find_element(*MainPageLocators.LAYER_TOGGLER)
        element.click()
    
    def set_bg_color(self, bg):
        element = self.driver.find_element(*MainPageLocators.BG_INPUT)
        # self.driver.execute_script('document.getElementsByName("color")[0].value="#fff000";')
        element.send_keys(f"{bg}")

    def toggle_paper_mode(self):
        element = self.driver.find_element(*MainPageLocators.FILTER_INPUT)
        element.click()

    def set_layer(self, bg:"color_code"="#ffffff"):
        # Layersパネルを開く
        self.open_layer_panel()
        # ペーパーモード解除
        self.toggle_paper_mode()

    def click_generate_button(self):
        """Triggers the design generator"""
        # デザインランダム生成
        element = self.driver.find_element(*MainPageLocators.GENERATE_BUTTON)
        element.click()

    def download_image(self):
        select_button = self.driver.find_element(*MainPageLocators.DOWNLOAD_SELECTOR)
        select_button.click()
        checkbox = self.driver.find_element(*MainPageLocators.TRANSPARENT_TOGGLER)
        checkbox.click()
        download_button = self.driver.find_element(*MainPageLocators.DOWNLOAD_BUTTON)
        download_button.click()