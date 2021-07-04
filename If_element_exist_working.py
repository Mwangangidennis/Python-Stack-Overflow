from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path='/home/denoh/Programs/Webdriver/chromedriver')
driver.implicitly_wait(0.5)
driver.get("https://www.tutorialspoint.com/index.htm")

# try except block
try:
    # identify element

    # l= driver.find_elements_by_css_selector("body > div:nth-child(2) > div > h4")
    l = driver.find_element_by_xpath('/html/body/div[2]/div/h4/mnh')
    print(l)
    # get list size with len
    s = 5
    # check condition, if list size > 0, element exists

    # if s > 0:
    m = l.text
    print("Element exist -" + m)
    # else:
except NoSuchElementException:
    print("Element does not exist")
driver.close()
