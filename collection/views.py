from datetime import datetime
from django.shortcuts import render
from collection.models import Products

# Create your views here.
def index(request):
    special_order = Products.objects.get(name="Yoshi")
    amigurumis = Products.objects.get(name="Baby Groot")
    baby_special = Products.objects.get(name="Pink Unicorn Crochet")
    decorations = Products.objects.get(name="Amigurumi Cactus")
    return render(request, 'index.html', {
        'now':datetime.now(),
        'special_order': special_order,
        'amigurumis':amigurumis,
        'baby_special':baby_special,
        'decorations':decorations,
    })
