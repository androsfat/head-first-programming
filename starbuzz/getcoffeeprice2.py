import urllib.request

page = urllib.request.urlopen("http://localhost/prices.html")
text = page.read().decode("utf8")

print(text)
