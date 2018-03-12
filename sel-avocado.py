from bs4 import BeautifulSoup
fp = open("fruits-vegetables.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

# select by css selector
print(soup.select_one("li:nth-of-type(8)").string)
print(soup.select_one("#ve-list > li:nth-of-type(4)").string)
print(soup.select("#ve-list > li[data-lo='us']")[1].string)
print(soup.select("#ve-list > li.black")[1].string)

# select by find method
cond = {"data-lo": "us", "class": "black"}
print(soup.find("li", cond).string)

# use find method successively
print(soup.find(id="ve-list")
          .find("li", cond).string)
