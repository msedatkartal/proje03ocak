from django.shortcuts import render,redirect # yönlendirme
from .models import *
# Create your views here.
def indexPage(request):
    content2 = Card.objects.filter(id = 2)
    news = Card.objects.filter(new = True)
    cards = Card.objects.all()
    news2 = news.order_by("?")[:2] #order_by = sıralama;
    category = Category.objects.all()
    context = {
        "content2": content2,
        "category" : category,
        "news4": news[:4],
        "news2": news2,
        "cards": cards,
    }
    return render(request,"index.html",context)

def detailPage(request,idc):
    card = Card.objects.get(id=idc)
    comments = Comment.objects.filter(card=card)
    
    if request.method == "POST":
        fname = request.POST.get("fname")
        text = request.POST.get("text")
        
        comment = Comment(fname=fname,text=text, card = card)
        comment.save()
        
        return redirect('/detail/'+ idc)
    context = {
        "card": card,
        "comments":comments,
    }
    return render (request,"detail.html",context)

def categoryPage(request,catetitle = None):
    # if cards = Card.objects.filter(category__title = catetitle).exists(): filtreleme yöntemi araştır!!!!! 
    if catetitle is None:
        cards = Card.objects.all()
    else:
        cards = Card.objects.filter(category__title = catetitle)
    category = Category.objects.all()
    context = {
        "cards" : cards,
        "category" : category,
    }
    return render (request,"category.html",context) 

def denemePage(request):
    
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        city = request.POST.get("city")

        print(fname,lname,city)
        
    return render (request,"deneme.html")