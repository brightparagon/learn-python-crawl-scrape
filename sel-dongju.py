from bs4 import BeautifulSoup
import urllib.request as req

url = "https://ko.wikipedia.org/wiki/%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

a_list = soup.select("#mw-content-text > div > ul > li a")

for a in a_list:
  name = a.string
  print("-", name)
