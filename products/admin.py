from django.contrib import admin

# Register your models here.
from .models import Category, Product, MainImage, FAQ, Size

admin.site.register([MainImage, FAQ, Size])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_name', 'slug']
	prepopulated_fields = {'slug': ('category_name',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 
	'description', 'pub_date', 'color']
	list_filter = ['color', 'pub_date', 'size']
	prepopulated_fields = {'slug': ('name',)}
