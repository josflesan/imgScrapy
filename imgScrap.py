# -*- coding: utf-8 -*-
"""
Google Image Python Scraper

@author: josflesan (github.com/josflesan)
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# helper libraries
import time
import io
import os
import requests
from PIL import Image


class GoogleImgScrapy:
    """
    Downloads images from google based on search term.
    driver - Selenium webdriver
    """

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        pass

    def _scroll_to_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    def _build_query(self, query: str):
        return f"https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={query}&oq={query}&gs_l=img"

    def _get_info(self, query: str):
        image_urls = set()

        self.driver.get(self._build_query(query))
        self._scroll_to_end()

        # img.Q4LuWd is google's thumbnail selector
        thumbnails = self.driver.find_elements_by_css_selector("img.Q4LuWd")

        print(f"Found {len(thumbnails)} images...")
        print(f"Getting the links...")

        try:
            thumbnails[0].click()  # Click on the first image
        except NoSuchElementException:
            print('ERROR: Cannot click on image')

        images = self.driver.find_elements_by_class_name('n3VNCb')  # Select image pop up
        time.sleep(0.3)

        if images[0].get_attribute('src') and 'http' in images[0].get_attribute('src'):
            image_urls.add(images[0].get_attribute('src'))

        return image_urls

    def download_image(self, folder_path: str, url: str):

        num = "01"

        try:
            image_content = requests.get(url).content

        except Exception as e:
            print(f"ERROR: Could not download {url} - {e}")

        try:
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file).convert('RGB')
            file = os.path.join(folder_path, num + '.jpg')

            with open(file, 'wb') as f:
                image.save(f, "JPEG", quality=85)
            print(f"SUCCESS: saved {url} - as {file}")

        except Exception as e:
            print(f"ERROR: Could not save {url} - {e}")

    def scrape_images(self, query: str, folder_path: str):
        folder = os.path.abspath(folder_path)

        if not os.path.exists(folder):
            os.makedirs(folder)

        image_info = self._get_info(query)
        print(f"Downloading images...")

        for image in image_info:
            self.download_image(folder, image)
