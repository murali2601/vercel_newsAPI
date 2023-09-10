from django.shortcuts import render
import requests


API_KEY = '943584be17604b20840422890cbd2951'
# Create your views here.
def home(request):

    url = f'https://newsapi.org/v2/everything?q=apple&from=2023-09-08&to=2023-09-08&sortBy=popularity&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    

    context = {
        'data' : data,
        'articles' : articles
    }
    
    return render(request,'base/home.html',context)


def category(request,category):

    url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {
        'category' : category.capitalize,
        'articles' : articles,

    }
    
    return render(request,'base/category.html',context)


