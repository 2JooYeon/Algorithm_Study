from selenium import webdriver

driver = webdriver.Chrome("C:/Users/InKyeong/Downloads/chromedriver_win32/chromedriver.exe")
url = 'https://www.seoulstore.com/categories/1000/recommend/desc'
driver.get(url)

btns= driver.find_elements_by_xpath('//div[@class=".Container .items .column.col-xs-6"]')
print("!!", len(btns))