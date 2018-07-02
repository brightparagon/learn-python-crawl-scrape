from selenium import webdriver
USER = 'kyeongmo2@naver'
PASS = 'brightParaGon*@'

# phantom driver
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

# access to login page
url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("Accessing to login page")

# input id and password
e = browser.find_element_by_id("id")
e.clear()
e.send_keys(USER)
e =  browser.find_element_by_id("pw")
e.clear()
e.send_keys(PASS)

# request login
form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print("Clicking login button")

# get data from shopping page
browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")

# print shopping list
products = browser.find_elements_by_css_selector(".p_info span")
print(products)
for product in products:
  print("-", product.text)
