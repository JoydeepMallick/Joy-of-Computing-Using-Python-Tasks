from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\JOYDEEP\Documents\COURSES 👀👀👀\NPTEL\2021\Joy of computing using python\python\wtsp automation\chromedriver.exe")

browser.get("https://www.google.com")

search = browser.find_element_by_name("q")

search.send_keys("oggy")
