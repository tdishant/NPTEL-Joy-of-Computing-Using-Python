from selenium import webdriverbrowser = webdriver.Chrome("/Users/mac/Downloads/chromedriver")browser.get("https://www.seleniumhq.org")elem = browser.find_element_by_link_text('MORE NEWS')elem.click()search = browser.find_element_by_class_name("form-control td-search-input ds-input")search.send_keys("Downloads")