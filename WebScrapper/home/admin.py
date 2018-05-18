from django.contrib import admin
from home.models import Search,SearchResult,SearchResultFlipkart,SearchV,VocabResults

# Register your models here.

admin.site.register(Search)
admin.site.register(SearchResult)
admin.site.register(SearchResultFlipkart)
admin.site.register(SearchV)
admin.site.register(VocabResults)
