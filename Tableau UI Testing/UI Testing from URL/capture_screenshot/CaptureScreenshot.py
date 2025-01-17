# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:34:30 2019

@author: Kalyani-Hemang
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import datetime
import util

class CaptureScreenshot(object):

    #Initialise google chrome webdriver
    def __init__(self):
        self.chrome_driver = os.getcwd() +"\\driver\\chromedriver.exe"
        self.load_headless_capture()
        capture_path = os.getcwd() + '\\temp\\'

        if not os.path.exists(capture_path):
            os.makedirs(capture_path)

    #Load headless webdriver
    def load_headless_capture(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')  # Last I checked this was necessary.
        chrome_options.add_argument("--window-size=1366x768")
        # self.driver = None
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=self.chrome_driver)
  
        
    def capture_screenshot(self,url,pos):
        # self.driver.get(url)

        driver = self.driver
        driver.maximize_window()
        driver.get(url)

        date_stamp = str(datetime.datetime.now()).split('.')[0]
        date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
        # file_name = os.getcwd() + '\\temp2\\' + date_stamp + ".png"
        # self.driver.get_screenshot_as_file(file_name)

        util.fullpage_screenshot(driver, pos)

        # return file_name