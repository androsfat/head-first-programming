import urllib.request
import time
import twitter

# My Twitter personal API keys
CONSUMER_KEY = 's8Rs4pS31m4u5jyYpPaiF7xsm' # Same as API key
CONSUMER_SECRET = 'JPe4yTPU1PELCIuVFdofXswuCppFJC8Gfyny6TbiaGFjjLbJ6H' # Same as API secret
ACCESS_TOKEN_KEY= '1118868396-Cn1MRYZeKRZxp519RAHjJpc8DLk9Z2cNzhHbqDk'
ACCESS_TOKEN_SECRET= 'yiiiOzNTEPS3WdNohDoAE0k8V0IFpENtqLByhon0BWApK'

def send_to_twitter(msg):
    if len(msg) > 140:
        raise Exception ('Message too long!')
    else:
        authkey = twitter.Twitter(auth=twitter.OAuth(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
        result = authkey.statuses.update(status=msg)
        return result

def get_price():
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return(float(text[start_of_price:end_of_price]))

price_now = input("Do you want to see the price now (y/n)? ")

if price_now == "y":
    msg = "The price of coffee beans is %s" % get_price() 
    # send_to_twitter(msg)
    send_to_twitter(str(get_price()))
    print(msg)
else:
    price = 99.99
    required_price = 6.00
    while price > required_price:
        time.sleep(15)
        price = get_price()
        print("Current price is: %s" % price)

    #     if price > required_price:
    #         print("Price is grater than %s" % required_price)

    msg = "The price of coffee beans is %s. Buy now!" % price
    # send_to_twitter(msg)
    send_to_twitter("Buy now!")
    print(msg)
