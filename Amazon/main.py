import os
try:
    import requests,re,json,random,sys
    from mahdix import *
    from datetime import datetime
    from mahdix import html as bs
    from concurrent.futures import ThreadPoolExecutor
    from time import sleep as slp
    from time import time as tim
except:
    os.system('pip insatll mahdix')
    os.system('pip insatll requests')
    os.system('pip insatll bs4')
from selenium import webdriver
clear()
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headers = {
    'authority': 'www.amazon.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7',
    'cache-control': 'max-age=0',
    'device-memory': '8',
    'downlink': '4.45',
    'dpr': '1',
    'ect': '4g',
    'rtt': '150',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '1',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-viewport-width': '661',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'viewport-width': '661',
}

chrome_options = Options()
driver = webdriver.Chrome()

driver.get('https://www.amazon.com')
sleep(10)
url='https://www.amazon.com/s?k=women+exercise+band&i=fashion-womens-jewelry&crid=3GQQ2UIKBKFTE&sprefix=women+exercise+band%2Cfashion-womens-jewelry%2C340&ref=nb_sb_noss_1'







import csv
headersx = [ "Handle","Title", "Published", "Option1 Name", "Option1 Value", 
"Option2 Name", "Option2 Value", "Variant Inventory Tracker",
"Variant Inventory Qty", "Variant Inventory Policy", 
"Variant Fulfillment Service", "Variant Price", "Variant Requires Shipping",
"Variant Taxable", "Image Src", "Image Position", "Description", "Status","Rating"]

file='output.csv'
#os.remove(file)

def save_to_csv(data_list):
    with open(file, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        #csv_writer.writerow(headers)
        csv_writer.writerows(data_list)
save_to_csv([headersx])
def price(html_content):
    soup = bs(html_content, 'html.parser')
    price_element = soup.find('span', {'class': 'a-offscreen'})
    price = price_element.text.strip() if price_element else None
    return price



def _of_data(responce):
    soup = bs(responce, 'html.parser')

    find_cls = soup.find_all('span', class_='a-color-base')


    # Extracting the rating (assuming it's the first span with class "a-size-base a-color-base")
    rating_span = soup.find('span', class_='a-size-base a-color-base')
    rating = rating_span.get_text(strip=True) if rating_span else None

    print("Rating:", rating)

    # Extracting the material
    material_span = soup.find('span', text='Material')
    material_value = material_span.find_next('span', class_='a-color-base').get_text(strip=True) if material_span else None

    print("Material:", material_value)

    # Extracting the product description
    description_span = soup.find('span', class_='a-list-item a-size-base a-color-base')
    description = description_span.get_text(strip=True) if description_span else None
    span_items = soup.find_all('span', class_='a-list-item a-size-base a-color-base')
    all_text_combined = ' '.join([span.get_text(strip=True) for span in span_items])

    return rating,description,all_text_combined

def g_data(p_url):
    #try:
        responce=requests.get(p_url,headers=headers,cookies=cookies).text
        sop=bs(responce,'html.parser')

        Title=sop.find('span',class_='a-size-large product-title-word-break').text.strip()
        Handle=Title.replace(' ','-')
        Published='true'
        Option1_Name='Product details'
        Option1_Value=_of_data(responce)[1]
        Rating=_of_data(responce)[0]
        Option2_Name='Size'
        try:
            ring_size_values = re.search('"ring_size":\s*\[([^\]]+)]', str(responce))
            if ring_size_values:
                Option2_Value = ring_size_values.group(1).replace('"', '').split(', ')
            else:
                Option2_Value = re.search('"size_name":\s*\[([^\]]+)]', str(responce)).group(1).replace('"', '').split(', ')
        except:Option2_Value=''

        Variant_Inventory_Tracker='Shopify'
        Variant_Inventory_Qty='1000'
        Variant_Inventory_Policy='deny'
        Variant_Fulfillment_Service='manual'
        Variant_Price=price(responce)
        Variant_Requires_Shipping='TRUE'
        Variant_Taxable='TRUE'
        Image_Src=[img.get('src') for img in sop.find('div', {'id': 'altImages'}).find_all('img')]
        Image_Position='1'
        Description=_of_data(responce)[2]
        Status='active'
        data = [ Handle, Title,Published, Option1_Name, Option1_Value, 
                Option2_Name, Option2_Value, Variant_Inventory_Tracker,
                Variant_Inventory_Qty, Variant_Inventory_Policy, 
                Variant_Fulfillment_Service, Variant_Price, Variant_Requires_Shipping,
                Variant_Taxable, Image_Src, Image_Position, Description, Status,Rating]

        save_to_csv([data])
   # except:print('error
driver.get(url)
sleep(15)
driver.execute_script("window.scrollBy(0, 500);")
sop=bs(driver.page_source,'html.parser')
all_link=sop.find_all('a',class_='a-link-normal s-no-outline')
clear()
cookies = driver.get_cookies()
formatted_cookie = ";".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
print(formatted_cookie)
print(mahdilinx())
for url in all_link:
    p_url='https://www.amazon.com'+url['href']
    g_data(p_url,formatted_cookie)
