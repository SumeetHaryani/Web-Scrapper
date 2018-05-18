import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests, bs4

def scrap():
    prod = []
    products_list = []
    prices_list = []
    while(len(prod)==0):
        res = requests.get('https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={}'.format(e.get()))
        bs = bs4.BeautifulSoup(res.text,'html.parser')
        # print(len(res.text))
        # print(res.text[:100])
        prod = bs.select("h2")
        price = bs.select(".s-price")
        # print(len(prod))
        try:
            for i in range(len(price)):
                products_list.append(prod[i].getText())
                prices_list.append(price[i].getText())
        except IndexError:
            print("No result found!!!")
            break

        for i in range(len(products_list)):
            print(products_list[i],"-->",prices_list[i])

def startScrap():
    print(e.get())
    print("Opening Amazon")
    browser = webdriver.Chrome("chromedriver.exe")
    browser.get("https://www.Amazon.in")
    name = browser.find_element_by_name("field-keywords")
    keyword = e.get()
    name.send_keys(keyword)
    browser.find_element_by_class_name('nav-input').click()


mw = tk.Tk()

mw.option_add("*Button.Background", "black")
mw.option_add("*Button.Foreground", "red")

mw.title('WEB SCRAPPING')

mw.geometry("500x500")
mw.resizable(0, 0)

back = tk.Frame(master=mw,bg='white')
back.pack_propagate(0)
back.pack(fill=tk.BOTH, expand=1)


info1 = tk.Label(master=back, text='Enter The Product name!', bg='red', fg='white')
info1.pack()
e=tk.Entry(master=back)
e.pack()
e.focus_set()
s=e.get()


go = tk.Button(master=back, text='Start Scrap', command=startScrap)
go.pack()
close = tk.Button(master=back, text='Quit', command=mw.destroy)
close.pack()
info = tk.Label(master=back, text='WEB SCRAPPING IN PYTHON!', bg='red', fg='white')
info.pack()

mw.mainloop()


# https://www.flipkart.com/search?q=macbook&otracker=start&as-show=on&as=off
# https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=macbook
