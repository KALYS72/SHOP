from django.contrib import admin
from .models import Category, Product
from review.models import Comment, Rate


class RateInLine(admin.TabularInline):
    model = Rate

class CommentInLine(admin.TabularInline):
    model = Comment



class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status']
    list_filter = ['category', 'status']
    search_fields = ['title', 'description']
    inlines = [CommentInLine, RateInLine]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)