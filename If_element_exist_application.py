from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path='/home/denoh/Programs/Webdriver/chromedriver')
driver.implicitly_wait(0.5)
driver.get("https://www.tutorialspoint.com/index.htm")

# try except block
z = 0

while z < 10:
    try:
        # identify element

        # l= driver.find_elements_by_css_selector("body > div:nth-child(2) > div > h4")
        l = driver.find_element_by_xpath('/html/body/div[2]/div/h4/bnb')
        print(l)
        # get list size with len
        s = 5
        # check condition, if list size > 0, element exists

        # if s > 0:
        m = l.text
        print("Element exist -" + m)
        # else:
        z = z + 1
        print(z)
    except NoSuchElementException:
        print("Element does not exist")
        z = z + 1
        print(z)
driver.close()
