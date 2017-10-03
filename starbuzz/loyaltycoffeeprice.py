import urllib.request

page = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
text = page.read().decode("utf8")

where= text.find(">$")

start_of_price = int(where) + 2
end_of_price = int(start_of_price) + 4

price = float(text[start_of_price:end_of_price])

print(price)
