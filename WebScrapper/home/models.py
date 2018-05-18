from django.db import models

# Create your models here.
class Search(models.Model):
    search_value = models.CharField(max_length = 264,unique = True)

    def __str__(self):
        return self.search_value

class SearchResult(models.Model):
    query = models.ForeignKey(Search)
    name = models.CharField(max_length = 100)
    price = models.CharField(max_length = 264)

    def __str__(self):
        return self.name

class SearchResultFlipkart(models.Model):
    queryF = models.ForeignKey(Search)
    nameF = models.CharField(max_length = 100)
    priceF = models.CharField(max_length = 264)
    def __str__(self):

        return self.nameF

class SearchV(models.Model):
    search_value = models.CharField(max_length = 264,unique = True)
    def __str__(self):
        return self.search_value

class VocabResults(models.Model):
    queryV = models.ForeignKey(SearchV)
    nameV = models.CharField(max_length = 500)
    def __str__(self):

        return self.nameV
