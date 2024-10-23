from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import json
try:
    json_data=open('is_pass_file.json','r',encoding='utf-8').read()
    data_list = json.loads(json_data)
except:
    print('File Not Fount');exit()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
new_data=[]
for id_pas in data_list:
    try:
        user_name=id_pas['email']
        password=id_pas['password']
        driver.get("https://twitter.com/i/flow/login")
        sleep(5)
        driver.find_element(By.CSS_SELECTOR, '#layers > div > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-14lw9ot.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div > div > div > div.css-175oi2r.r-1f1sjgu.r-mk0yit.r-13qz1uu > label').send_keys(user_name)
        btns = driver.find_element(By.XPATH, '//div[@role="button"]//*[text()="Next"]').click()
        sleep(1)
        driver.find_element("name","password").send_keys(password)
        sleep(1)
        button_xpath = '//div[@data-testid="LoginForm_Login_Button"]'
        login_button = driver.find_element(By.XPATH, button_xpath)
        login_button.click()
        sleep(2)
        cookies = driver.get_cookies()
        formatted_cookies = ";".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
        if 'ct0' in formatted_cookies:
            print(formatted_cookies)
            new_data.append(formatted_cookies.replace('"',''))
        driver.delete_all_cookies()
    except:pass
try:
    with open('cookes.json',"w",encoding="utf-8") as file:
        json_data = json.dump(new_data ,file ,ensure_ascii=False, indent=4)
        file.close()
except Exception as e: print(e)
driver.quit()