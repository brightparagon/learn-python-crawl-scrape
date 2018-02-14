from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <h1 id="title">scrape?</h1>
    <p id="body">analyze web pages</p>
    <p>extract parts needed</p>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
title = soup.find(id="title")
body = soup.find(id="body")

print("title = ", title.string)
print("body = ", body.string)
