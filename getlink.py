from lxml import html
import requests
page = requests.get('https://www.primeabgb.com/buy-online-price-india/graphic-cards-gpu/page/2/', verify=False)
tree = html.fromstring(page.content)
price = tree.xpath('//div[@class="text-center product-details"]/div[@class="product-title"]/a/@href')
print (price)

