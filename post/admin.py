from django.contrib import admin
from .models import Article,ArticleImage,ArticleCategory,PacketsUsers,PacketsArticle

# Register your models here.
class ImageInlines(admin.TabularInline):
    model = ArticleImage
    extra = 2
    min_num =0
    max_num = 15
 

@admin.register(ArticleCategory)
class CategoryArticle(admin.ModelAdmin):
    list_filter=["product","category"]
    list_display=["product","category"]

    class Meta:
        model = ArticleCategory




@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_filter=["created_date","qiymet"]
    list_display=["title","author","created_date"]
    list_display_links=["title"]
    search_fields=["title",'content']
    inlines = [ImageInlines]

    class Meta:
        model=Article

@admin.register(ArticleImage)
class AdminArticleImage(admin.ModelAdmin):

    class Meta:
        model = ArticleImage

@admin.register(PacketsUsers)
class AdminUserPacket(admin.ModelAdmin):
    search_fields=['packet']
    list_display=['user','packet']

    class Meta:
        model = PacketsUsers

@admin.register(PacketsArticle)
class AdminArticlePacket(admin.ModelAdmin):
    search_fields=["packet"]
    list_display=['elan','packet']

    class Meta:
        model = PacketsArticle

