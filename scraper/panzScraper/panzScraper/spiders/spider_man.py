import scrapy
from scrapy_playwright.page import PageMethod
from playwright.sync_api import Playwright
from scrapy.http import Response, Request, HtmlResponse
from panzScraper.items import ProductItem
import random
import requests
import os

class SpiderManSpider(scrapy.Spider):
    name = "spider_man"
    allowed_domains = ['pancernik.eu', 'trustmate.io']
    start_urls = ["https://pancernik.eu/"]
    #AI generated User-agents used randomly to prevent Timeout/IP ban
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

    #Taking all available categories from menu, parsing each one of them
    def parse(self, response: Response):
        page_urls = response.css("a.row ::attr(href)").getall()
        #Shooting for all available categories from Menu
        categories_url = response.css("div.innerbox ul.standard li a::attr(href)").getall()
        categories_names = response.css("div.innerbox ul.standard li a::text").getall()
        #first category has specific structure, different from others so we sip that
        categories_url.pop(0) 
        categories_names.pop(0) 
        for cat_url in categories_url:
            url = self.start_urls[0] + cat_url
            yield Request(url, callback = self.parse_category, headers={"User-Agent": self.user_agents[random.randint(0, len(self.user_agents)-1)]})
            
    #As we are already inside specific category, we choose every subcategory available
    def parse_category(self, response: Response):
        subcategories_url = response.css("div.all div a::attr(href)").getall()
        for sub_url in subcategories_url:
            url = self.start_urls[0] + sub_url
            yield Request(url, callback = self.parse_subcategory, headers={"User-Agent": self.user_agents[random.randint(0, len(self.user_agents)-1)]})

    #For each subcategory scrape every product on the stock, separately for product data and images of product
    def parse_subcategory(self, response:Response): 
        products_id = response.css("div.products div.product::attr(data-product-id)").getall()
        prod_urls = response.css("a.prodname ::attr(href)").getall()
        prod_categories = response.url.replace(self.start_urls[0], "").split('/')
        for index, prod_id in enumerate(products_id):
            url_data = f"https://pancernik.eu/webapi/front/pl_PL/products/PLN/{prod_id}" #template url for product data
            url_img = self.start_urls[0]+ prod_urls[index]
            #There must be two different requests, because of images absence on the data page
            yield Request(url_img, callback=self.save_images, headers={"User-Agent": self.user_agents[random.randint(0, len(self.user_agents)-1)]}, meta = {"id" : prod_id})
            yield Request(url_data, callback=self.parse_product, headers={"User-Agent": self.user_agents[random.randint(0, len(self.user_agents)-1)]}, meta={'categories' : prod_categories})

    #Shoots request for url with product data, then we create model object [ProductItem] based on response which will be parsed and validated in [pipelines.py] 
    def parse_product(self, response : Response):
        body_json = response.json()
        product = ProductItem()
        product["id"] = body_json["id"]
        product["name"]= body_json["name"]
        product["ean"]= body_json["ean"]
        product["rate"] = body_json["rate"]
        product["votes"] = body_json["votes"]
        product["category"] = response.meta.get('categories')
        product["availability"]= body_json["availability"]
        product["delivery"]= body_json["delivery"]
        product["gross"] = body_json["price"]
        product["net"] = body_json["price"]
        product["weight"] = body_json["weight"]
        product["producer"] = body_json["producer"]
        product["description"] = self.parse_description(body_json)
        yield product
        
    #Scrapes images url from product gallery, then shoot each one of them, saving fetched images to dedicated directory ["/images/{product_id}"] 
    def save_images(self, response:Response):
        urls = response.css("a.gallery ::attr(href)").getall()
        image_urls = list(dict.fromkeys(urls)) #uniqe img urls
        os.mkdir(os.getcwd() + f"/images/{response.meta.get('id')}") #creating uniqe directory for product images
        for index, img_url in enumerate(image_urls):
            url = self.start_urls[0] + img_url
            resp = requests.get(url)
            filename = os.path.join(os.getcwd()+f"/images/{response.meta.get('id')}/",f"{index+1}.jpg")
            with open (filename, 'wb') as file:
                file.write(resp.content)

    #Reduces all trash characters from scraped product descripton, simplifies it 
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
