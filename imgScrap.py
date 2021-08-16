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
        image_url = ''

        self.driver.get(self._build_query(query))
        self._scroll_to_end()

        # img.Q4LuWd is google's thumbnail selector
        thumbnail = self.driver.find_element_by_css_selector("img.Q4LuWd")

        print(f"Getting the link...")

        try:
            thumbnail.click()  # Click on the first image
        except NoSuchElementException:
            print('ERROR: Cannot click on image')

        image = self.driver.find_element_by_class_name('n3VNCb')  # Select image pop up
        time.sleep(0.5)

        if image.get_attribute('src') and 'http' in image.get_attribute('src'):
            image_url = image.get_attribute('src')

        return image_url

    def _get_mult_info(self, query: str, num_images: int):
        image_urls = []

        self.driver.get(self._build_query(query))
        self._scroll_to_end()

        # img.Q4LuWd is google's thumbnail selector
        thumbnails = self.driver.find_elements_by_css_selector("img.Q4LuWd")

        print(f"Getting the links...")

        for thumbnail in thumbnails[0:num_images+1]:
            try:
                thumbnail.click()  # Click on the first image

                images = self.driver.find_elements_by_class_name('n3VNCb')  # Select image pop up
                time.sleep(0.3)

                for image in images:
                    if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                        image_urls.append(image.get_attribute('src'))

            except NoSuchElementException:
                print('ERROR: Cannot click on image')

        return image_urls

    def download_image(self, query: str, folder_path: str, url: str):

        try:
            image_content = requests.get(url).content

        except Exception as e:
            print(f"ERROR: Could not download {url} - {e}")

        try:
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file).convert('RGB')
            file = os.path.join(folder_path, query + '.jpg')

            with open(file, 'wb') as f:
                image.save(f, "JPEG", quality=85)
            time.sleep(0.3)
            print(f"SUCCESS: saved {url} - as {file}")

        except Exception as e:
            print(f"ERROR: Could not save {url} - {e}")

    def scrape_single_images(self, queryList: list, folder_path: str):
        folder = os.path.abspath(folder_path)
        image_urls = []

        if not os.path.exists(folder):
            os.makedirs(folder)

        for query in queryList:
            image_url = self._get_info(query)
            image_urls.append(image_url)

        print(f"Downloading image...")

        for query, url in zip(queryList, image_urls):
            self.download_image(query, folder, url)

    def scrape_many_images(self, queryList: list, folder_path: str, num_images: int):
        folder = os.path.abspath(folder_path)
        image_urls = {}
        queryPos = 0

        if not os.path.exists(folder):
            os.makedirs(folder)

        for query in queryList:
            image_urls[query] = self._get_mult_info(query, num_images)

        print(f"Downloading images...")
        print(image_urls)

        for query in image_urls.keys():
            queryPos = 0
            for url in image_urls[query]:
                self.download_image(query + str(queryPos), folder, url)
                queryPos += 1
