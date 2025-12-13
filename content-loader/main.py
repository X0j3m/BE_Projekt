import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

files_path = "content"
url_api = "http://localhost:8080/api/"
api_key = "73LWQPLCQF5LH7UKK8LHPL22ZGVYQMZB"
headers = {'Content-Type': 'application/xml'}


def read_csv(filename) -> np.ndarray:
    df = pd.read_csv(f"{files_path}/{filename}.csv")
    return df.to_numpy()

def create_request(resource, request):
    response = requests.post(
        url_api + resource,
        data=request,
        auth=(api_key, ''),
    )
    soup = BeautifulSoup(response.text, features="xml")

    tag = soup.find('id')
    return tag.get_text()

def create_product(product_name, active, price, tax_group, category_id):
    request=f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
      <product>
        <id_shop_default>1</id_shop_default>
        <name>
          <language id="1">{product_name}</language>
        </name>
        <description_short>
          <language id="1"></language>
        </description_short>
        <description>
          <language id="1"></language>
        </description>
        <active>{active}</active>
        <price>{price}</price>
        <id_tax_rules_group>{tax_group}</id_tax_rules_group>
        <show_price>1</show_price>
        <depends_on_stock>0</depends_on_stock>
        <id_category_default>2</id_category_default>
        <link_rewrite>
          <language id="1">{trasform_to_link_rewrite(product_name)}</language>
        </link_rewrite>
        <associations>
          <categories>
            <category>
              <id>{category_id}</id>
            </category>
          </categories>
        </associations>    
      </product>
    </prestashop>
    """.strip()
    return create_request("products", request)

def create_category(category_name, active, parent_id):
    request = f"""
        <?xml version="1.0" encoding="UTF-8"?>
        <prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
            <category>
                <id_parent>{parent_id}</id_parent>
                <active>{active}</active>
                <is_root_category>0</is_root_category>
                <name>
                    <language id="1">{category_name}</language>
                </name>
                <link_rewrite>
                    <language id="1">{trasform_to_link_rewrite(category_name)}</language>
                </link_rewrite>
                <meta_title>
                    <language id="1">{category_name}</language>
                </meta_title>
            </category>
        </prestashop>
        """.strip()
    return create_request("categories", request)

def trasform_to_link_rewrite(text):
    link_rewrite = text.lower().replace(" ", "-")
    return link_rewrite


def main():
    categories = read_csv("cateogries")
    for category in categories:
        id = create_category(category[2], category[1], 2)
        category[0] = id

    subcategories = read_csv("subcategories")
    for subcategory in subcategories:
        parent_cat_id = categories[categories[:, 2] == subcategory[3]][0][0]
        id = create_category(subcategory[2], subcategory[1], parent_cat_id)
        subcategory[0] = id

    products = read_csv("products2")
    for product in products:
        try:
            cat_id = subcategories[subcategories[:, 2] == product[3]][0][0]
            id = create_product(product[1], product[2], 0, 1, cat_id)
            product[0] = id
        except:
            pass

if __name__ == '__main__':
    main()
