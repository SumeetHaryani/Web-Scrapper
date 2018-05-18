from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models
# Create your views here.

# import tkinter as tk
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import requests, bs4
def scrapAmazon(param,t):
    print("In Amazon")
    prod = []
    products_list = []
    prices_list = []
    while(len(prod)==0):
        print("************************************************")
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        res = requests.get('https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={}'.format(param),headers=headers)
        bs = bs4.BeautifulSoup(res.text,'html.parser')
        # print(len(res.text))
        # print(res.text)
        prod = bs.select(".s-access-title")
        price = bs.select(".s-price")

        try:
            for i in range(len(price)):
                # print(prod[i])

                products_list.append(prod[i].getText()[:100] + "...")
                prices_list.append(price[i].getText())

        except IndexError:
            print("No result found!!!")

        l = []
        for i in range(len(products_list)):

            l += [[products_list[i],prices_list[i]]]
            search_model = models.SearchResult.objects.get_or_create(query =t, name = products_list[i],price = prices_list[i])[0]
            search_model.save()
            # print("<-----------Added to Database--------------->")
            # print(products_list[i],"-->",prices_list[i])
# https://www.flipkart.com/search?q=mitv
        return(l)

def scrapFlipkart(param,t):
    print("In flipkart")
    prod = []
    products_list = []
    prices_list = []
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    while(len(prod)==0):
        res = requests.get('https://www.flipkart.com/search?q={}'.format(param),headers=headers)
        bs = bs4.BeautifulSoup(res.text,'html.parser')
        print(len(res.text))
        # print(res.text[:100])
        prod = bs.select("._3wU53n")
        # price = list(set(bs.select("._1vC4OE")).intersection(set(bs.select("._2rQ-NK"))))
        price = bs.select("._1vC4OE")


        if (len(prod)==0 or len(price)==0):
            prod = bs.select("._2cLu-l")
            price = bs.select("._1vC4OE")

        try:
            for i in range(len(prod)):
                # print(price[i])
                products_list.append(prod[i].getText()[:100] + "...")
                prices_list.append(price[i].getText())
        except IndexError:
            print("No result found!!!")
            break
        print(len(products_list),len(prices_list))
        l = []
        for i in range(len(products_list)):
            # print(products_list[i],"-->",prices_list[i])
            l += [[products_list[i],prices_list[i]]]
            search_m = models.SearchResultFlipkart.objects.get_or_create(queryF =t, nameF = products_list[i],priceF = prices_list[i])[0]
            # print(search_m)
            search_m.save()

            # print("<-----------Added to Database--------------->")
        return(l)


def vocabs(request):
    form = forms.FormName()
    t = None
    if request.method == 'POST':
        form = forms.FormName(request.POST)

    if form.is_valid():
        print("validation successfull")
        s = form.cleaned_data['search']
        t = models.SearchV.objects.get_or_create(search_value = s)[0]
        t.save()
        scrapVocab(s,t)

    if t==None:
        search_result = []
        search_result_F = []
    print(t)

    search_result_V = models.VocabResults.objects.filter(queryV = t)
    my_dict = {'insert_me':"Now I am coming from first_app/index.html!"
                    ,'forms':form,
                    'recordsV':search_result_V,
                    }
#    return render(request,'home/main.html',context=my_dict)
    return render(request, "home/vocabs.html",context=my_dict)

def scrapVocab(param,t):

    res=requests.get("https://en.oxforddictionaries.com/definition/{}".format(param))
    soup=bs4.BeautifulSoup(res.text,"html.parser")
    vocab=soup.select('.ind')
    meaning_list=[]
    try:
        for i in range(len(vocab)):
            meaning_list.append(vocab[i].getText())
        print(meaning_list)

    except IndexError:
        print("No result found!!!")

    for i in range(len(meaning_list)):
        search_model = models.VocabResults.objects.get_or_create(queryV =t, nameV = meaning_list[i],)[0]
        search_model.save()
        print("<-----------Added to Database--------------->")
        print(meaning_list[i])

def images(param):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    res = requests.get('https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={}'.format(param),headers=headers)
    bs = bs4.BeautifulSoup(res.text,'html.parser')
    image = bs.select(".s-access-image")
    print(image[0])
    im= []
    try:
        for i in range(3):
            im.append(image[i].get('src'))
    except IndexError:
        print("No Result")
    # print(len(prod))
    # print(prod,price)
    return(im)

def index(request):
    form = forms.FormName()
    t = None

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("validation successfull")
            s = form.cleaned_data['search']
            t = models.Search.objects.get_or_create(search_value = s)[0]
            t.save()
            search_result = scrapAmazon(s,t)
            imageArray = images(param=s)
            search_result_F = scrapFlipkart(s,t)
    if t==None:
        search_result = []
        search_result_F = []
        imageArray = []
    # print(t)
    # print(search_result_F)
    my_dict = {'insert_me':"Now I am coming from first_app/index.html!"
                ,'forms':form,
                'recordsA':search_result,
                'recordsF':search_result_F,
                'imgA':imageArray,}
    return render(request,'home/main.html',context=my_dict)

def intro(request):
    d = {}
    return render(request,'home/intro.html',context = d)
def aboutus(request):
    d = {}
    return render(request,'home/aboutus.html',context = d)
