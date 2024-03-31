from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    fields = ['title', 'body', 'author', 'slug', 'approved', 'pdf', 'email', 'organization']
    actions = ['approve_articles']

    def approve_articles(self, request, queryset):
        queryset.update(approved=True)
    approve_articles.short_description = "Approve selected articles"

# Register the ArticleAdmin class for the Article model
admin.site.register(Article, ArticleAdmin)

# Customize admin site headers
admin.site.site_header = 'Confex Administration'
admin.site.site_title = 'Confex Admin'
admin.site.index_title = 'Confex Admin Dashboard'
