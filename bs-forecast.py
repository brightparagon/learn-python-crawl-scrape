from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# get data using urlopen
res = req.urlopen(url)

# analyze it using BeautifulSoup
soup = BeautifulSoup(res, "html.parser")

# extract data from soup
title = soup.find("title").string
wf = soup.find("wf").string
print(title)
print(wf)
