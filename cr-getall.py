from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

# variable: to check if it is processed already
proc_files = []

# function: extract links inside html
def enum_links(html, base):
  soup = BeautifulSoup(html, "html.parser")
  links = soup.select("link[rel='stylesheet']") # CSS
  links += soup.select("a[href]") # link
  result = []

  for a in links:
    href = a.attrs['href']
    url = urljoin(base, href)
    result.append(url)
  
  return result

# function: download and save fiels
def download_file(url):
  o = urlparse(url)
  savepath = "./" + o.netloc + o.path
  if re.search(r"/$", savepath): # if folder
    savepath += "index.html"
  savedir = os.path.dirname(savepath)

  if os.path.exists(savepath): return savepath
  
  # creat a folder
  if not os.path.exists(savedir):
    print("mkdir=", savedir)
    makedirs(savedir)

  # download files
  try:
    print("download=", url)
    urlretrieve(url, savepath)
    time.sleep(1)
    return savepath
  except:
    print("download fail", url)
    return None
