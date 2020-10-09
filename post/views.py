from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from . import models
from user import forms
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    keyword = request.GET.get("s")

    if  keyword:

        
        articles = models.Article.objects.filter(title__contains=keyword)[::-1]
        if articles==False:
            return render(request,"searchIndex.html")
        if len(articles)>4:
            palasa = len(articles)//4 + 1
            print(palasa)
            x = 0
            
            son=[]
            for i in range(palasa):
                son+=[articles[x:x+4]]
                x+=4

                        #articles = get_object_or_404(models.Article,title__contains=keyword) Bele de munkundur.
            return render(request,"searchIndex.html",{
            "son":son
            })

        else:
            


            return render(request,"searchIndex.html",{
            "son":[articles]
            })



    articles = models.Article.objects.all()[::-1] # [:10] Butun Articllar Sonuncu 10 dene
    
    palasa = len(articles)//4 + 1
    print(palasa)
    x = 0
    
    son=[]
    for i in range(palasa):
        son+=[articles[x:x+4]]
        x+=4

    


    return render(request,"index.html",{
    "son":son
    })




def about(request):
    contex={
        "salam":"salam",
        "sifre":1234,
    }
    return render(request,"about.html",contex)

def dynamic(request,id):
    articlenow = get_object_or_404(models.Article,id=id)
    article = get_object_or_404(models.Article,id=id)
    try:
        articleImages=models.ArticleImage.objects.filter(product = articlenow)
        print(articleImages,'\n',articleImages[0].product_image.url,"BUUUUU ARTICCCLEEE IMAGEESSSDIR")
        content = {
            'article':article,
            'articleImages':articleImages
        }

        return render(request,"product.html",content)
    except:

        print(article.title,article.content,"VARYOXXXXXXX")

        content = {
            "article":article
        }

        return render(request,"product.html",content)


def create(request):
    keyword = request.GET.get("s")

    if  keyword:

        
        articles = models.Article.objects.filter(title__contains=keyword)
        palasa = len(articles)//4 + 1
        print(palasa)
        x = 0
        
        son=[]
        for i in range(palasa):
            son+=[articles[x:x+4]]
            x+=4

                    #articles = get_object_or_404(models.Article,title__contains=keyword) Bele de munkundur.



        return render(request,"searchIndex.html",{
        "son":son[::-1]
        })



    articles = models.Article.objects.all() # Butun Articllar Sonuncu 10 dene
    articles = articles[::-1]
    palasa = len(articles)//4 + 1
    print(palasa)
    x = 0
    
    son=[]
    for i in range(palasa):
        son+=[articles[x:x+4]]
        x+=4

    


    return render(request,"check.html",{
    "son":son
    })

@login_required(login_url="/user/login")
def deleteArticle(request,id):
    
    article = get_object_or_404(models.Article,id=id)
    if article.author == request.user:
        article.delete()

        messages.success(request, 'Elan Silindi')


        return redirect("user:dashboard")
    else:
        messages.warning(request, 'Bu Meqaleni Silenmersen !!')


        return redirect("user:dashboard")

@login_required(login_url="/user/login")
def updateArticle(request,id):
    
    if request.method == "POST":
        
        form = forms.StickerForm(request.POST,request.FILES)

        if form.is_valid():
            Sticker = form.save(commit=False)
            Sticker.author = request.user

            imgHead = request.FILES.get("image")
            ctgry = request.POST.get("status")

            fs = FileSystemStorage()
            file_path=fs.save(imgHead.name,imgHead)

            Sticker.image = file_path 

            Sticker.save()

            ac  = models.ArticleCategory()

            ac.product = Sticker
            ac.category= ctgry

            ac.save()


            try:
                files = request.FILES.getlist("file[]")
                for img in files:
                    print (img)
                    newfs=FileSystemStorage()
                    newPath= newfs.save(img.name,img)



                    newImage = models.ArticleImage(product=Sticker,product_image=newPath)
                    newImage.save()
                    
                link = "/sticker/"+str(Sticker.id)
                return redirect(link)



            except:



                link = "/sticker/"+str(Sticker.id)
                return redirect(link)


    article = get_object_or_404(models.Article,id=id)
    form = forms.StickerForm(instance=article)
        
    return render(request,"updateArticle.html",{"form":form})