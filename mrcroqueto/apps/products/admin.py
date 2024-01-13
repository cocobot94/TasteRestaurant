from django.contrib import admin
from .models import Products, CategoryProduct
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class ProductsResources(resources.ModelResource):
    class Meta:
        model = Products


class CategoryResources(resources.ModelResource):
    class Meta:
        model = CategoryProduct


class ProductsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("name", "price", "get_category")
    search_fields = ["name"]
    resource_class = ProductsResources

    def get_category(self, obj):
        return ", ".join(
            categories.description for categories in obj.category_product.all()
        )

    get_category.short_description = "category"


class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["description"]
    resource_class = CategoryResources


admin.site.register(Products, ProductsAdmin)
admin.site.register(CategoryProduct, CategoryAdmin)
