from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm,searchForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def amina(request):
    form =searchForm(request.POST or None)
    ville = "casa"
    print("METHOD:", request.method)
    print("POST:", request.POST)
    if request.method=="POST":
        if "ville" in request.POST :
            print("ok")
            if form.is_valid():
                ville=form.cleaned_data["ville"]
                ville=ville.capitalize()
                if ville=="0":
                    ville="(choisit une ville stp)"
                
                print("ville choisie:", ville)

    context = {"form":form, "ville":ville,  "prix":20, "unites":"150 km"}
    return render(request, 'blog/HOME.html', context)





def home(request):
    context={"var":30}
    
    return render(request, 'blog/home2.html', context)

def contact(request):
    var = '''
    salut tous le monde
    vous allez bien
    youpiiiiii
    
    '''
    context={"var":var}
    return render(request, 'blog/contact.html', context)

def calcul(request):
    context={"re":"salut toi"}
    return render(request, 'blog/calcul.html', context)







"""
type de variables : texte, numeric, binary...
creer une variable
operateurs de comparaisons 
difference entre liste [], dictionnaire {}, tupple()
indentation
print
imports 

plus tard:
conditionnel
boucles

function

dates
df
class

"""