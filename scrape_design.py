import unittest
from selenium import webdriver
from mypackage import page
import time
import sys

def main():
    max_num = int(sys.argv[1])
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://iterograph.laboiteatortue.com/#/") 
    main_page = page.MainPage(driver)
    main_page.set_layer()
    for i in range(max_num):
        #Sets the text of search textbox to "pycon"
        main_page.click_generate_button()
        main_page.download_image()
        time.sleep(1)
    driver.close()

if __name__ == '__main__':
    main()