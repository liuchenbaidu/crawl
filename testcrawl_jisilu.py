from selenium import webdriver
browser = webdriver.Chrome()
url = 'https://www.jisilu.cn/data/cbnew/#cb'
browser.get(url)
data = browser.page_source
import pandas as pd
tables = pd.read_html(data)
for i in range(len(tables)):
    print(i)
    print(tables[i])
