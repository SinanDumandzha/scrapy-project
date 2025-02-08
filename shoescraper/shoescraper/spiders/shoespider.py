import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from shoescraper.items import ShoeItem
import re

class ShoeSpider(scrapy.Spider):
    name = "shoespider"
    allowed_domains = ["www.academy.com"]

    def start_requests(self):
        url = "https://www.academy.com/p/nike-womens-court-legacy-next-nature-shoes"
        yield SeleniumRequest(url=url, callback=self.parse, wait_time=10)
    
    def parse(self, response):
        driver = response.request.meta["driver"]
        driver.maximize_window()
        driver.implicitly_wait(10)

        shoe_item = ShoeItem()

        shoe_item['name'] = driver.find_element(By.CSS_SELECTOR, "#pdp240TitleWrapper > h1").text
        shoe_item['price'] = driver.find_element(By.CSS_SELECTOR, ".pricing").text
        shoe_item['colour'] = driver.find_element(By.CSS_SELECTOR, ".swatchName--KWu4Q").text
        shoe_item['availableColours'] = self.getAvailableColours(driver)
        shoe_item['reviews_count'] = driver.find_element(By.CSS_SELECTOR, '.ratingCount').text
        shoe_item['reviews_score'] = driver.find_element(By.CSS_SELECTOR, '.ratingAvg').text

        yield shoe_item

    def getAvailableColours(self, driver):
        buttons = driver.find_elements(By.CSS_SELECTOR, "#swatch-drawer-content button")
        availableColours = []

        for button in buttons:
            aria_label = button.get_attribute("aria-label")

            if aria_label:
                aria_label = " ".join(aria_label.split())
                color_name = re.sub(r"\b(Color|selected|Clearance)\b", "", aria_label, flags=re.IGNORECASE).strip()
                availableColours.append(color_name)

        return availableColours