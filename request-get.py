import requests
r = requests.get("http://api.aoikujira.com/time/get.php")

# text
text = r.text
print(text)

# binary
bin = r.content
print(bin)