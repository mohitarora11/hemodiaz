from django.contrib import admin
from models import Product, Category,  Subcategory, Aboutus



class ProductAdmin(admin.ModelAdmin):
    list_display = ['subcategory','product_name','product_desc','prod_image','inserteddate','status']
    search_fields = ['product_name']
    class Media:
        js = ['/media/tiny_mce/tiny_mce.js','/media/js/admin.js']


admin.site.register(Product, ProductAdmin)
    
admin.site.register(Category)


class AboutAdmin(admin.ModelAdmin):
    class Media:
        js = ['/media/tiny_mce/tiny_mce.js','/media/js/admin.js']
        
        
admin.site.register(Aboutus,AboutAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['c_name','category','sortorder']

admin.site.register(Subcategory,SubCategoryAdmin)