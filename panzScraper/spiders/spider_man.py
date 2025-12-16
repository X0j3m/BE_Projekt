import scrapy
from playwright.sync_api import sync_playwright, Playwright
from scrapy.http import Response, Request, HtmlResponse
from panzScraper.items import ProductItem
import random
import requests
import os
import csv
from bs4 import BeautifulSoup
import re
class SpiderManSpider(scrapy.Spider):
    name = "spider_man"
    allowed_domains = ['pancernik.eu']
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
    cats = []
    sub_cats = []

    #Taking all available categories from menu, parsing each one of them
    def parse(self, response: Response):
        page_urls = response.css("a.row ::attr(href)").getall()
        #Shooting for all available categories from Menu
        categories_url = response.css("div.innerbox ul.standard li a::attr(href)").getall()
        categories_names = response.css("div.innerbox ul.standard li a::text").getall()
        #first category has specific structure, different from others so we sip that
        categories_url.pop(0) 
        categories_names.pop(0)
       #for i, cat_url in enumerate(categories_url):
        url = self.start_urls[0] + categories_url[5]
        self.cats.append(categories_names[5])
        yield scrapy.Request(url, callback = self.parse_category, headers={"User-Agent": self.user_agents[random.randint(0, len(self.user_agents)-1)]})

    #As we are already inside specific category, we choose every subcategory available
    def parse_category(self, response: Response):
        subcategories_url = response.css("div.all div a::attr(href)").getall()
        subcategories_names = response.css("div.all div a img::attr(alt)").getall()
        parsed_sub_cats=[]
        for sub_cat in subcategories_names:
              soup = BeautifulSoup(sub_cat, 'html.parser')
              raw_text = soup.get_text()
              cleaned_text = re.sub(r'\s+', ' ', raw_text).strip()
              parsed_sub_cats.append(cleaned_text)
        self.sub_cats.append(parsed_sub_cats)
        for i, sub_url in enumerate(subcategories_url):
            if i==1:
                break
            if self.start_urls[0] in sub_url:
                url = sub_url
            else:
                url = self.start_urls[0] + sub_url
            sub_cat_name = parsed_sub_cats[i]
            yield scrapy.Request(url, callback = self.parse_subcategory, headers={"User-Agent": self.user_agents[random.randint(0, len(self.user_agents)-1)]}, meta={'category_name' : sub_cat_name})

    #For each subcategory scrape every product on the stock, separately for product data and images of product
    def parse_subcategory(self, response:Response):
        products_id = response.css("div.products div.product::attr(data-product-id)").getall()
        prod_urls = response.css("a.prodname ::attr(href)").getall()
        for index, prod_id in enumerate(products_id):
            url_data = f"https://pancernik.eu/webapi/front/pl_PL/products/PLN/{prod_id}" #template url for product data
            url_img = self.start_urls[0]+ prod_urls[index]
            #There must be two different requests, because of images absence on the data page
            yield scrapy.Request(url_img, callback=self.save_images, headers={"User-Agent": self.user_agents[random.randint(0, len(self.user_agents)-1)]}, meta = {"id" : prod_id})
            yield scrapy.Request(url_data, callback=self.parse_product, headers={"User-Agent": self.user_agents[random.randint(0, len(self.user_agents)-1)]}, meta={'category_name' : response.meta.get('category_name')})

    #Shoots request for url with product data, then we create model object [ProductItem] based on response which will be parsed and validated in [pipelines.py] 
    def parse_product(self, response : Response):
        img_urls = []
        body_json = response.json()
        img_urls.append(f"http://localhost/prestashop/img/p/{body_json['id']}/{body_json['id']}.jpg")
        product = ProductItem()
        product["id"] = body_json["id"]
        product["name"]= body_json["name"]
        product["active"] = 1
        product["category"] = response.meta.get('category_name')
        product["description"] = self.parse_description(body_json)
        product["net"], product["gross"] = self.parse_prices(body_json)
        product["weight"] = self.parse_weight(body_json=body_json)
        product["available"] = random.randint(0,10)
        yield product
        
    #Scrapes images url from product gallery, then shoot each one of them, saving fetched images to dedicated directory ["/images/{product_id}"] 
    def save_images(self, response:Response):
        urls = response.css("a.gallery ::attr(href)").getall()
        image_urls = list(dict.fromkeys(urls)) #uniqe img urls
        os.mkdir('/home/rys/scrap/BE_Projekt/scraper/panzScraper/panzScraper' + f"/images/{response.meta.get('id')}") #creating uniqe directory for product images
        for index, img_url in enumerate(image_urls):
            if index == 2: #we are saving only 2 photos per product
                break
            url = self.start_urls[0] + img_url
            resp = requests.get(url)
            #TODO In the future, when Scraper branch will be merched with devel, change path directly to PrestaShop/img
            filename = os.path.join('/home/rys/scrap/BE_Projekt/scraper/panzScraper/panzScraper'+f"/images/{response.meta.get('id')}/",f"{index+1}.jpg")
            with open (filename, 'wb') as file:
                file.write(resp.content)
    #Reduces all trash characters from scraped product descripton, simplifies it 
    def parse_description(self, body_json):
        raw_description = body_json["description"]
        soup = BeautifulSoup(raw_description, 'html.parser')

        # Użycie .get_text() do ekstrakcji całej zawartości tekstowej z pominięciem tagów
        raw_text = soup.get_text()
        cleaned_text = re.sub(r'\s+', ' ', raw_text).strip()
        pattern = r'[^\w\s.,:?!()*\-]'
        # Usunięcie niedozwolonych znaków (zastąpienie ich pustym ciągiem)
        cleaned_string_temp = re.sub(pattern, '', cleaned_text, flags=re.UNICODE)

        # Opcjonalnie: Usunięcie nadmiarowych spacji, które mogą powstać po usunięciu symboli
        cleaned_string = re.sub(r'\s+', ' ', cleaned_string_temp).strip()
        return cleaned_string
    
    def parse_prices(self, body_json):
        prices = body_json['price']
        netto = prices['net']
        gross = prices['gross']
        return (netto['base_float'], gross['base_float'])

    def parse_weight(self, body_json):
        weight = body_json["weight"]
        return weight['weight_float'] 
    
    def closed(self, response):
        sub_res = self.sub_cats
        print(sub_res)
        cat_id = 10
        sub_cat_id = 20
        filename = "/home/rys/scrap/BE_Projekt/scraper/panzScraper/panzScraper/spiders/categories.csv"
        filename2 = "/home/rys/scrap/BE_Projekt/scraper/panzScraper/panzScraper/spiders/subcategories.csv"
        with open (filename, 'w') as file, open(filename2, 'w') as file2:
            csvwriter = csv.writer(file, delimiter=',')
            csvwriter2 = csv.writer(file2, delimiter=',')
            csvwriter.writerow(['ID', 'Aktywny', 'Nazwa', 'Kategoria nadrzędna'])
            csvwriter2.writerow(['ID', 'Aktywny', 'Nazwa', 'Kategoria nadrzędna'])
            for index, cat in enumerate(self.cats):
                tmp = []
                tmp.append(cat_id)
                cat_id+=1
                tmp.append(1)
                tmp.append(cat)
                tmp.append('Home')
                csvwriter.writerow(tmp)
                print(f"WYSWIETLAM LISTE PODKATEGORI DLA {cat}")
                print(sub_res[index])
                for sc in sub_res[index]:
                    tmp2 = []
                    tmp2.append(sub_cat_id)
                    sub_cat_id+=1
                    tmp2.append(1)
                    tmp2.append(sc)
                    tmp2.append(cat)
                    csvwriter2.writerow(tmp2)
