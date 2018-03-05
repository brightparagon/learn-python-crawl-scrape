from bs4 import BeautifulSoup
import urllib.request as req

# get html
url = "http://info.finance.naver.com/marketindex/"
res = req.urlopen(url)

# analyze html
soup = BeautifulSoup(res, "html.parser")

# extract data
price = soup.select_one("div.head_info > span.value").string
print("usd/krw =", price)
