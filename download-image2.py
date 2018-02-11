import requests
r = requests.get("http://wikibook.co.kr/wikibook.png")

# save an image as a form of binary
with open("test.png", "wb") as f:
  f.write(r.content)

print("saved!")