from django.shortcuts import render
from .models import Bureau
from .models import Chambre
from .models import Salon


def bureau(request):
    return render(request, 'pagesproduit/bureau.html',{'pro':Bureau.objects.all()})
def chambre(request):
    return render(request, 'pagesproduit/chambre.html',{'chambre':Chambre.objects.all()})
def salon(request):
    return render(request, 'pagesproduit/salon.html',{'salon':Salon.objects.all()})

def description(request):
    # Récupération des paramètres depuis l'URL
    image = request.GET.get('image')
    nom = request.GET.get('nom')
    desc = request.GET.get('desc')


    return render(request, 'pagesproduit/description.html', {
        'image': image,
        'nom': nom,
        'desc': desc,
    })


