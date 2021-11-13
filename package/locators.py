from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    LAYER_TOGGLER = (By.XPATH, "//a[@class='accordion-toggle' and contains(., 'Layers')]")
    BG_INPUT = (By.XPATH, "//input[@type='color' and @ng-model='graph.style.background']")
    FILTER_INPUT = (By.XPATH, "//input[@type='checkbox' and @ng-model='graph.style.filtered']")
    GENERATE_BUTTON = (By.XPATH, "//button[contains(., 'Generate a new design')]")
    DOWNLOAD_SELECTOR = (By.XPATH, "//button[@ng-controller='ModalDownloadCtrl']")
    DOWNLOAD_BUTTON = (By.XPATH, "//button[contains(., 'Download') and @type='button']")
    TRANSPARENT_TOGGLER = (By.XPATH, "//input[@type='checkbox' and @ng-model='transparent']")

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass