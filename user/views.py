from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from . import forms
from django.contrib.auth.models import User
# Create your views here.
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
#from django.shortcuts import HttpResponseRedirect
from post.models import Article,ElanCategory,ArticleImage,ArticleCategory,PacketElan,PacketsArticle,PacketsUsers,Elan,ElanImage
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required



def UserLogout(request):
    logout(request)
    messages.success(request,"Hesabinizdan Cixis Etdiniz")
    return redirect("index")

    
def register(request):
    if request.method=="POST":
        try:
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data.get("first_name")
                last_name = form.cleaned_data.get("last_name")            
                username = form.cleaned_data.get("username")
                email = form.cleaned_data.get("email")
                password = form.cleaned_data.get("password")

                newUser = User(first_name=first_name,last_name=last_name,username=username,email=email)
                newUser.set_password(password)
                newUser.save()

                Packet= PacketsUsers()
                Packet.user=newUser
                Packet.packet='nrml'
                Packet.save() 
                

                messages.success(request, 'Qeydiyatdan Ugurla Kecdiniz !')

                return redirect("index")
        except:
            messages.warning(request, 'Bele Isdifadeci Adi Artiq Movcuddur!')

            return redirect("/user/register")
        else:

            form = forms.RegisterForm()

            content={
                "form":form
            }

            messages.warning(request, 'Parollari Duzgun Yazin')
            return render(request,"register.html",content)
    else:
        form = forms.RegisterForm()

        content={
            "form":form
        }

        return render(request,"register.html",content)

def LoginUser(request):
    form = forms.LoginForm(request.POST or None)

    content = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        

        newUser = authenticate(request,username=username,password=password)

        if newUser is None:


            messages.warning(request, 'Isdifadeci Adi Veya Parol Yanlisdir')
            return render(request,"login.html",content)

        messages.success(request, 'Ugurla Daxil Oldunuz')
        login(request,newUser)

        return redirect("index")


  

    return render(request,"login.html",content)


@login_required(login_url="/user/login")
def dashboard(request):
    keyword=request.GET.get("elan")
    print(keyword)
    if keyword:
        articles = Article.objects.filter(author=request.user,title__contains=keyword)[::-1]
        
        return render(request,'dashboard.html',{"articles":articles})



    articles = Article.objects.filter(author=request.user)
    print(articles,"ARTICLEESS")
    content = {

        "articles":articles[::-1],

    }






    return render(request,"dashboard.html",content)



@login_required(login_url='/user/login')
def vip(request):


    content={
        "vip":'salam'
    }

    return render(request,"vip.html",content)





@login_required(login_url="/user/login")
def sticker(request):
    if request.method == "POST":
        form = forms.StickerForm(request.POST,request.FILES)

        if form.is_valid():
            Sticker = form.save(commit=False)
            Sticker.author = request.user
            imgHead = request.FILES.get("image")
            ctgry = request.POST.get("status")
            Sticker.status = ctgry

            fs = FileSystemStorage()
            file_path=fs.save(imgHead.name,imgHead)

            Sticker.image = file_path 



            #Sticker.product = Article.objects.get(id=Sticker.id)
    
            Sticker.save()
            Packet = PacketsArticle()
            Packet.elan=Sticker
            Packet.packet='nrml'
            Packet.save()
            ac  = ArticleCategory()

            ac.product = Sticker
            ac.category= ctgry
            ac.save()


            try:
                files = request.FILES.getlist("file[]")
                for img in files:
                    print (img)
                    newfs=FileSystemStorage()
                    newPath= newfs.save(img.name,img)



                    newImage = ArticleImage(product=Sticker,product_image=newPath)
                    newImage.save()
                    
                return redirect(reverse('dynamic',kwargs={"id":Sticker.id})) # burda dynamic esas url faylinda oldugu ucun qabaqina isaBlog yazilmir cunki main di ozu birinci ora baxir



            except:



                return redirect(reverse('dynamic',kwargs={"id":Sticker.id}))
      


    form = forms.StickerForm()
    content={
        "form":form,
    }
    
        
    return render(request,"sticker.html",content)


def elan(request):
    if request.method == "POST":
        form = forms.ElanForm(request.POST,request.FILES)

        if form.is_valid():
            Sticker = form.save(commit=False)
            imgHead = request.FILES.get("image")
            ctgry = request.POST.get("status")
            Sticker.status = ctgry

            fs = FileSystemStorage()
            file_path=fs.save(imgHead.name,imgHead)

            Sticker.image = file_path 



            #Sticker.product = Article.objects.get(id=Sticker.id)
    
            Sticker.save()

            
            Packet = PacketElan()
            Packet.elan=Sticker
            Packet.packet='nrml'    #Burdaki Olanlar Elan ucunde yaratmaq lazimdi
            Packet.save()
            
            
            ac  = ElanCategory()

            ac.product = Sticker
            ac.category= ctgry
            ac.save()
            


            try:
                files = request.FILES.getlist("file[]")
                for img in files:
                    print (img)
                    newfs=FileSystemStorage()
                    newPath= newfs.save(img.name,img)



                    newImage = ElanImage(product=Sticker,product_image=newPath)
                    newImage.save()
           
                messages.success(request, 'Elanınız Uğurla yerləsdirildi')
                return redirect(reverse('user:elanDinamik',kwargs={"id":Sticker.id}))



            except:


                messages.success(request, 'Elanınız Uğurla yerləsdirildi')
                return redirect(reverse('user:elanDinamik',kwargs={"id":Sticker.id}))  
                #burda reverse user in icerisindeki urls baxir ve adi elanDinamik olan urlni cagiriri ve yaninada id ni yerlesdirir
        messages.warning(request, '"Məhsul Haqqında" Bölməsini doldurmalısınız')
        return redirect('/user/elan')
    
    
    else:

        form=forms.ElanForm()

        

        return render(request,"Elan.html",{"form":form})


def elanDinamik(request,id):

    articlenow = get_object_or_404(Elan,id=id)

    try:
        articleImages=ElanImage.objects.filter(product = articlenow)
        print(articleImages,'\n',articleImages[0].product_image.url,"BUUUUU ARTICCCLEEE IMAGEESSSDIR")
        content = {
            'article':articlenow,
            'articleImages':articleImages,
        }

        return render(request,"product.html",content)
    except:


        content = {
            "article":articlenow,
        }

        return render(request,"product.html",content)