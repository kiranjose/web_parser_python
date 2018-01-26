import  urllib.request
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()
temp = urllib.request.urlopen('https://www.primeabgb.com/online-price-reviews-india/galax-geforce-gtx-1070-oc-mini-8gb-gddr5-graphic-card', context=context)
HTML = temp.read().decode("utf-8")
words = ['ADATA', 'Email for price', 'Add to cart']
for word in words:
    if word in HTML:
       print("found             ", word)
    else:
       print("not found         ",word)
