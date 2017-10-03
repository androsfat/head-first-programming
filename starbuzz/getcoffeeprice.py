import urllib.request

page = urllib.request.urlopen("http://localhost/prices-loyalty.html")
text = page.read().decode("utf8")
price = text[178:182]
print(price)
