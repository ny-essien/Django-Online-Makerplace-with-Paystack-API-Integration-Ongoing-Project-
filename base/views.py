from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Category,Item

# Create your views here.
def homepage(request : HttpRequest):
    
    items = Item.objects.filter(is_sold = False)[:6]
    categories = Category.objects.all()

    content = {

        'categories' :categories,
        'items' : items
    }

    return render(request, 'base/home.html', content)


def contact(request):

    return render(request, 'base/contacts.html')


def detailPage(request, pk):

    item = get_object_or_404(Item, pk = pk)
    related_items = Item.objects.filter(category = item.category, is_sold = False).exclude(pk = pk)[:3]

    context = {

        'item': item,
        'related_items' : related_items
    }
    return render(request, 'base/detail.html', context )

