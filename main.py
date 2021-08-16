"""
Main Program to run image scraper
Implementation based on tutorial @ https://rubikscode.net/2021/06/21/scraping-images-with-python/

@author josflesan (github.com/josflesan)
"""

from imgScrap import GoogleImgScrapy

DRIVER_PATH = './webdriver/chromedriver.exe'
IMG_PATH = 'C:/Users/josue/Documents/Programming/projects/imgScrapy/img'
QUERIES = ['kanye']


def main():
    goog_scraper = GoogleImgScrapy(DRIVER_PATH)

    # Maximum of 15 images per query for optimum performance
    goog_scraper.scrape_images(QUERIES, 'C:/Users/josue/Documents/Programming/projects/imgScrapy/img', 15)


if __name__ == "__main__":
    main()
