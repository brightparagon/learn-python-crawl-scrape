import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# parameter url encode
values = {
  'stnId': '108'
}
params = urllib.parse.urlencode(values)
url = API + "?" + params
print("url=", url)

# download
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
