"""
Main Program to run image scraper
Implementation based on tutorial @ https://rubikscode.net/2021/06/21/scraping-images-with-python/

@author josflesan (github.com/josflesan)
"""

from imgScrap import GoogleImgScrapy

DRIVER_PATH = './webdriver/chromedriver.exe'
IMG_PATH = 'C:/Users/josue/Documents/Programming/projects/imgScrapy/img'
QUERIES = ['music']


def main():
    goog_scraper = GoogleImgScrapy(DRIVER_PATH)
    goog_scraper.scrape_many_images(QUERIES, 'C:/Users/josue/Documents/Programming/projects/imgScrapy/img', 10)


if __name__ == "__main__":
    main()
