from bs4 import BeautifulSoup

# html to be analyzed
html = """
<html><body>
<div id="meigen">
  <h1>wiki book</h1>
  <ul class="items">
    <li>unity game</li>
    <li>swift</li>
    <li>web</lib>
  </ul>
</div>
</body></html>
"""

# analyze html
soup = BeautifulSoup(html, 'html.parser')

# select using css query
h1 = soup.select_one("div#meigen > h1").string
print("h1 =", h1)

li_list = soup.select("div#meigen > ul.items > li")
for li in li_list:
  print("li =", li.string)
