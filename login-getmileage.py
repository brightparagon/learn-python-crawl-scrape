import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

USER = "<TEST>"
PASS = "<TEST>"

# start a session
session = requests.session()

# login
login_info = {
  "m_id": USER,
  "m_passwd": PASS
}
