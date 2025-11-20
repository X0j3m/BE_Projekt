import scrapy
from scrapy_playwright.page import PageMethod
from playwright.sync_api import Playwright
from scrapy.http import Response, Request, HtmlResponse
import random
import requests
import os

class SpiderManSpider(scrapy.Spider):
    name = "spider_man"
    allowed_domains = ['pancernik.eu', 'trustmate.io']
    start_urls = ["https://pancernik.eu/"]
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.78 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.91 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.11 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/115.0',
        'Mozilla/5.0 (Linux; Android 12; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.5253.124 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile Safari/604.1',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36'
    ]


    #"https://pancernik.eu/main_wg-modelu"
    def parse(self, response: Response):
        page_urls = response.css("a.row ::attr(href)").getall()

        #Shooting for all available categories from Menu
        categories_url = response.css("div.innerbox ul.standard li a::attr(href)").getall()
        categories_url.pop(0)
        for cat_url in categories_url:
            url = self.start_urls[0] + cat_url
            yield Request(url, callback = self.parse_category, headers={"User-Agent": self.user_agents[random.randint(0, len(self.user_agents)-1)]})
            
    def parse_category(self, response: Response):
        subcategories_url = response.css("div.all div a::attr(href)").getall()
        for sub_url in subcategories_url:
            url = self.start_urls[0] + sub_url
            yield Request(url, callback = self.parse_subcategory, headers={"User-Agent": self.user_agents[random.randint(0, len(self.user_agents)-1)]})

    def parse_subcategory(self, response:Response):
        products_id = response.css("div.products div.product::attr(data-product-id)").getall()
        for prod_id in products_id:
            url = f"https://pancernik.eu/webapi/front/pl_PL/products/PLN/{prod_id}"
            yield Request(url, callback=self.parse_product, headers={"User-Agent": self.user_agents[random.randint(0, len(self.user_agents)-1)]})

    def parse_product(self, response : Response):
        save_path = '/images'
        body_json = response.json()
        product = {
            "id" : body_json["id"],
            "name": body_json["name"],
            "ean": body_json["ean"],
            "rate" : body_json["rate"],
            "votes" : body_json["votes"],
            "category" : body_json["category"],
            "availability": body_json["availability"],
            "delivery" : body_json["delivery"],
            "price" : body_json["price"],
            "weight" : body_json["weight"],
            "producer" : body_json["producer"],
            "description" : self.parse_description(body_json),
        }
        self.save_images(body_json)
        yield product
        
    def save_images(self, body_json):
        description = body_json['description'].split(" ")
        images_urls = [i for i in description if "src" in i]
        images_urls = [i.split("=") for i in images_urls]
        images_urls = [i[1] for i in images_urls]
        for index, img_url in enumerate(images_urls):
            url = img_url.replace('"', '')
            resp = requests.get(url)
            filename = os.path.join(os.getcwd()+"/images/",f'{body_json["id"]}_{index+1}.jpg')
            with open (filename, 'wb') as file:
                file.write(resp.content)

    def parse_description(self, body_json):
        raw_description = body_json["description"]
        resp = HtmlResponse(url="myHtml", body = raw_description, encoding= 'utf-8')
        features = resp.css("p").getall()
        features = [f.replace("<strong>", "") for f in features]
        features = [f.replace("</strong>", "") for f in features]
        features = [f.replace("<p>", "") for f in features]
        features = [f.replace("</p>", "") for f in features]
        features = [f for f in features if "img" not in f]
        return features


