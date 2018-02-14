from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <h1>scrape?</h1>
    <p>analyze web pages</p>
    <p>extract parts needed</p>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

print("h1 = ", h1.string)
print("p = ", p1.string)
print("p = ", p2.string)