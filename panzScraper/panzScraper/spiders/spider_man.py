import scrapy
from scrapy_playwright.page import PageMethod
from playwright.sync_api import Playwright
from scrapy.http import Response, Request

class SpiderManSpider(scrapy.Spider):
    name = "spider_man"
    allowed_domains = ['pancernik.eu', 'trustmate.io']
    start_urls = ["https://pancernik.eu/"]

    def parse(self, response: Response):
        page_urls= response.css("a.row ::attr(href)").getall()
        #TODO scraping category/subcategory/and them products
        # response.css("div.innerbox ul.standard li a::attr(href)").getall() ---->>> getting all categories urls
        ## response.css("div.all div a img::attr(alt)").get() <<<<<<>>>>>>> get the name of subcategory
        ## response.css("div.all div a::attr(href)").get()  <<<<<<>>>>>>> get url of subcategory
        ### response.css("div.grid-mob div a::text").getall()  <<<<<<>>>>>>> get list of subcategories name
        ### response.css("div.grid-mob div a::attr(href)").getall()  <<<<<<>>>>>>> get list of subcategories urls
        #### response.css("div.products") <<<<<<<>>>>>>> get list of products [ raw html ]

        #Shooting for all available categories from Menu
        categories_url = response.css("div.innerbox ul.standard li a::attr(href)").getall()
        for cat_url in categories_url:
            url = self.start_urls[0] + cat_url
            yield Request(url, callback = self.parse_category)
            
    def parse_product(self, response:Response):
        product = {
            "title": response.css("h1.name ::text").get(),
            "price": response.css("div.price em.main-price ::text").get(),
            "availability": response.css("div.row span.second ::text").get(),
            "delivery_time": response.css("div.delivery span.second ::text").get(),
            "EAN_code": response.css("div.productdetails-more h2.code span ::text").get(),
            "producent": response.css("div.manufacturer a.brand ::text").get()
        }
        product_id = response.css("div.votestars span::attr(data-id-product)").get()

        if product_id:
            rating_url = f"https://pancernik.eu/webapi/front/pl_PL/products/PLN/{product_id}"
            yield Request(
                rating_url,
                headers={"Accept": "*/*", "Referer": response.url},
                callback=self.parse_rating,
                meta={"product": product} 
            )
        else:
            yield product


    def parse_rating(self, response : Response):
        body_json = response.json()
        product = {
            "name": body_json["name"],
            "ean": body_json["ean"],
            "code" : body_json["code"],
            "rate" : body_json["rate"],
            "category" : body_json["category"],
            "availability": body_json["availability"],
            "delivery" : body_json["delivery"],
            "price" : body_json["price"],
            "weight" : body_json["weight"],
            "producer" : body_json["producer"],
            "description" : body_json["description"],
            "attributes" : body_json["attributes"],
            "images" : body_json["images_filename"]
        }
        yield product

    def parse_category(self, response: Response):
        subcategories_url = response.css("div.all div a::attr(href)").getall()
        for sub_url in subcategories_url:
            url = self.start_urls[0] + sub_url
            yield Request(url, callback = self.parse_subcategory)

    def parse_subcategory(self, response:Response):
        


