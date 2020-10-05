from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.

STATUS_CHOICES = [
    ('e', 'Elektronika'),
    ('evb', 'Ev Ve Bag'),
    ('se', 'Sexsi Esyalar'),
    ('n', 'Neqliyat'),
    ('da', 'Dasinmaz Emlak'),
    ('hvn', 'Heyvanlar'),
]


class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Isdifadeci")
    title = models.CharField(max_length=50,verbose_name="Basliq")
    content = RichTextField(verbose_name="Mehsul Hakkinda")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Yaradilma Tarixi")
    status = models.CharField(max_length=3,choices=STATUS_CHOICES,default='')
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
       




class ArticleCategory(models.Model):
    product = models.ForeignKey('Article',on_delete=models.CASCADE)
    category = models.CharField(max_length=50,choices=STATUS_CHOICES,verbose_name="Category")

    def __str__(self):
        return self.category
    