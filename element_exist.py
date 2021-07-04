from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/denoh/Programs/Webdriver/chromedriver')
driver.implicitly_wait(0.5)
driver.get("https://www.tutorialspoint.com/index.htm")
# identify element
# l= driver.find_elements_by_css_selector("body > div:nth-child(2) > div > h4")
l = driver.find_element_by_xpath('/html/body/div[2]/div/h4')
print(l)
# get list size with len
s = 5
# check condition, if list size > 0, element exists

if s > 0:
    m = l.text
    print("Element exist -" + m)
else:
    print("Element does not exist")
driver.close()
