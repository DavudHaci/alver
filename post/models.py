from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.

STATUS_CHOICES = [
    ('e', 'Elektronika'),
    ('evb', 'Ev Ve Bag'),
    ('se', 'Sexsi Esyalar'),
    ('n', 'Neqliyat'),
    ('da', 'Dasinmaz Emlak'),
    ('hvn', 'Heyvanlar'), # Categoriyalarin hamisini Bir bir yaz ! amk
    ('tlf','Telefonlar')
]

USER_PACKETS = [

    ('nrml','Normal'),
    ('vip','VIP'),
    ('dmnd','DIAMOND'),
    ('pre','PREMIUM'),

]

ARTICLE_PACKETS=[
    ('nrml','Normal'),
    ('vip','VIP'),
    ('dmnd','DIAMOND'),
    ('pre','PREMIUM'),
]





class Elan(models.Model):
    user = models.CharField(max_length=50,verbose_name="İsdifadəçi Adı")
    title = models.CharField(max_length=50,verbose_name="Başlıq Yazısı ")
    content = RichTextField(verbose_name="Mehsul Haqqında")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Yaradilma Tarixi")
    status = models.CharField(max_length=3,choices=STATUS_CHOICES,verbose_name='category',default=None)
    nomre = models.IntegerField(verbose_name="Telefon Nömrəsi")
    image = models.ImageField(blank=True,verbose_name="Səkil Əlavə Et")
    qiymet = models.IntegerField(verbose_name="Qiymət")
    

    
    def __str__(self):
        return self.title





class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Isdifadeci")
    title = models.CharField(max_length=50,verbose_name="Basliq")
    content = RichTextField(verbose_name="Mehsul Hakkinda")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Yaradilma Tarixi")
    status = models.CharField(max_length=3,choices=STATUS_CHOICES,verbose_name='category',default=None)
    nomre = models.IntegerField(verbose_name="Telfon Nomresi")
    image = models.ImageField(blank=True,verbose_name="Sekil Elave Et")
    qiymet = models.IntegerField(verbose_name="Qiymet")
    

    
    def __str__(self):
        return self.title




class ArticleImage(models.Model):
    product = models.ForeignKey('Article',on_delete=models.CASCADE) 
    product_image = models.ImageField(blank=True,upload_to="images/")

    def __str__(self):
        return self.product.title + "Image"


class ElanImage(models.Model):
    product = models.ForeignKey('Elan',on_delete=models.CASCADE) 
    product_image = models.ImageField(blank=True,upload_to="images/")

    def __str__(self):
        return self.product.title + "Image"
       




class ArticleCategory(models.Model):
    product = models.ForeignKey('Article',on_delete=models.CASCADE)
    category = models.CharField(max_length=50,choices=STATUS_CHOICES,verbose_name="Category")

    def __str__(self):
        return self.category
    



class PacketsUsers(models.Model):
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Isdifadeci")
    packet = models.CharField(choices=USER_PACKETS,verbose_name="Paketler",default="Normal",max_length=50)
    
    def  __str__(self):
        return self.user.username
    
class PacketsArticle(models.Model):
    elan = models.ForeignKey("Article",on_delete=models.CASCADE,verbose_name="Elan")
    packet = models.CharField(choices=ARTICLE_PACKETS,verbose_name="Paketler",default="Normal",max_length=50)
    def  __str__(self):
        return self.elan.title
