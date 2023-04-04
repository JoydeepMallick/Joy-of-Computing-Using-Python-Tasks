from selenium import webdriver

browser =  webdriver.Chrome(r"C:\Users\JOYDEEP\Documents\COURSES 👀👀👀\NPTEL\2021\Joy of computing using python\python\wtsp automation\chromedriver.exe")

browser.get("https://www.seleniumhq.org")

ele = browser.find_element_by_link_text("Download")
elem.click()

search = browser.find_element_by_id("q")
# inspect the seleniumhq page and find the search bar element

search.send_keys("Download")

