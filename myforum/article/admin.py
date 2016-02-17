from django.contrib import admin
from models import Article

class ArticleAdmin(admin.ModelAdmin):
	list_display=("title","block","owner","create_timestamp","last_update_timestamp")
	search_fields=["title","content","owner"]
	list_filter=("block",)

admin.site.register(Article,ArticleAdmin)