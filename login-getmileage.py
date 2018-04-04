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
url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
res.raise_for_status()

# access to mypage
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()

# get mileage and ecoin
soup = BeautifulSoup(res.text, "html.parser")
mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()
print("milage: ", mileage)
print("ecoi: ", ecoin)
