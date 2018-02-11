import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "text.png"

# download an image and put it on the memory
mem = urllib.request.urlopen(url).read()

with open(savename, mode="wb") as f:
  f.write(mem)
  print("saved!")
