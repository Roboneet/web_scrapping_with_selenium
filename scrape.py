from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#replace
chrome_path = r"/Users/joyp.isahac/Downloads/chromedriver"

driver = webdriver.Chrome(chrome_path)
driver.get("http://www.ndtv.com/latest")
headings = driver.find_elements_by_class_name("nstory_header")
for heading in headings:
    print(heading.text)
driver.quit()