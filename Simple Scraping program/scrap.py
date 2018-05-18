import requests, bs4
prod = []
products_list = []
prices_list = []
while(len(prod)==0):
    res = requests.get('https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=oneplus')
    bs = bs4.BeautifulSoup(res.text,'html.parser')
    print(len(res.text))
    print(res.text[:100])
    prod = bs.select("h2")
    price = bs.select(".s-price")
    print(len(prod))
    for i in range(len(price)):
        products_list.append(prod[i].getText())
        prices_list.append(price[i].getText())

for i in range(len(products_list)):
    print(products_list[i],"-->",prices_list[i])

# <span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>56,990</span>
