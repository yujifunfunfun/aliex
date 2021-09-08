import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import eel
import time
from logger import *
import csv
import re
import random

logger = set_logger(__name__)

def start_chrome():
    user_agent = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    ]
    UA = user_agent[random.randrange(0, len(user_agent), 1)]
    global option
    option = Options()                         
    option.add_argument('--lang=ja-JP')
    option.add_argument('--user-agent=' + UA)
    option.add_argument('--ignore-certificate-errors')
    option.add_argument('--ignore-ssl-errors')
    option.add_argument('--incognito') 
    option.add_argument("window-size=1300,1000")
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)   


def fetch_item_data(category,keyword,delete_keyword,min_price,max_price,free_delivery,evaluation,min_sales_figures,max_sales_figures):
    try:
        # 出品画面へ遷移
        driver.get("https://ja.aliexpress.com/")
        logger.info('リクエスト受付中ページへ遷移しました')
        eel.view_log_js('リクエスト受付中ページへ遷移しました')
        time.sleep(3)

        if category == "":
            pass
        else:
            driver.find_element_by_xpath(f'//*[@id="search-dropdown-box"]/option[text()="{category}"]').click()
        
        if keyword == "":
            pass
        else:
            driver.find_element_by_id('search-key').send_keys(keyword)
            driver.find_element_by_class_name("search-button").click()

        if delete_keyword == "":
            pass
        else:
            delete_keyword_list = delete_keyword.split('\n')

        if min_price == "":
            pass
        else:
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/span[1]/span[2]/input').send_keys(min_price)
        if max_price == "":
            driver.find_element_by_class_name("ui-button narrow-go").click()
        else:               
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/span[1]/span[3]/input').send_keys(max_price)
            driver.find_element_by_class_name("ui-button narrow-go").click()
       
        if free_delivery == "":
            pass
        else:
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/span[2]/span[2]/label/span[1]/input').click()
        
        if evaluation == "":
            pass
        else:        
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/span[2]/span[3]/label/span[1]/input').click()

        if max_sales_figures:
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[1]/span[2]/span[2]').click()

        item_lists = driver.find_elements_by_class_name("_2mXVg")

        # 販売個数取得
        sales_figures_lists = driver.find_elements_by_class_name("_2i3yA")
        sales_counts_lists = []
        for sales_figures in sales_figures_lists:
            sales_figures = sales_figures.text
            p = r'(.*) 個販売'
            sales_figures = re.search(p, sales_figures).group(1)
            sales_counts_lists.append(int(sales_figures))
        
        for item,sales_counts in zip(item_lists,sales_counts_lists):
            # 価格と除外キーワードで絞り込み
            if min_sales_figures <= sales_counts <= max_sales_figures and len([i for i in delete_keyword_list if i in item.text]) == 0:
                item_url = item.get_attribute("href")
                driver.get(item_url)
                item_title = driver.find_elements_by_class_name("product-title-text").text
                item_min_price = 
                item_max_price = 
                postage = 




    except Exception as e:
        logger.info(e)
        eel.view_log_js('エラーが発生しました')
        driver.quit()



def main(category,keyword,delete_keyword,min_price,max_price,free_delivery,evaluation,min_sales_figures,max_sales_figures):
    start_chrome()
    fetch_item_data(category,keyword,delete_keyword,min_price,max_price,free_delivery,evaluation,min_sales_figures,max_sales_figures)
        
# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
