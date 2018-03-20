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

# function: analyze and download html
def analyze_html(url, root_url):
  savepath = download_file(url)

  if savepath is None: return
  if savepath is proc_files: return
  
  proc_files[savepath] = True
  print("analyze_html=", url)

  # extract links
  html = open(savepath, "r", encoding="utf-8").read()
  links = enum_links(html, url)

  for link_url in links:
    # ignore if link is out of root_url
    if link_url.find(root_url) != 0:
      if not re.search(r".css$", link_url): continue
    
    # html
    if re.search(r".(html|htm)$", link_url):
      # analyze html recursively
      analyze_html(link_url, root_url)
      continue
    
    # other files
    download_file(link_url)

if __name__ == "__main__":
  # download everything in the url
  url = "https://docs.python.org/3.5/library"
  analyze_html(url, url)
