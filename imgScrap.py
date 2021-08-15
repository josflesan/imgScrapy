# -*- coding: utf-8 -*-
"""
Google Image Python Scraper

@author: josflesan (github.com/josflesan)
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

# helper libraries
import time
import urllib.request
import os
import requests
from PIL import Image


class GoogleImgScrapy:

    DRIVER_PATH = './webdriver'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=GoogleImgScrapy.DRIVER_PATH)
        pass

    def saveImages(self, image_urls: list):
        pass

    def findImages(self):
        pass

    def saveMultiple(self, img_path: str, search_keys: list):
        pass

    def saveOne(self, img_path: str, search_key: str):
        pass







