from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.core import serializers
from .dataHelper import magicCardsDataRequest, magicSetsDataRequest
from .models import mtgCard, mtgSet
# Create your views here.

#similar to a controller or list of controllers


#learning how to return content from a url
def index(request):
    magicCardsDataRequest()
    magicSetsDataRequest()
    return HttpResponse("Data Loaded!")

#called from the form submit on the home page
#takes the two inputs from the form and passes them to the search method
#provides results for the frontend to display
def search(request):
    searchTerm = request.POST.get('searchTerm')
    searchType = request.POST.get('searchType')
    searchResults = keywordSearch(searchTerm, searchType)
    searchResultsJson = serializers.serialize('json', searchResults)
    dynamicData = {'data': searchResults}
    return render(request,'search.html', context=dynamicData)


#app landing page, contains input field for search
def home(request):
    return render(request, 'home.html')


#query the database for searchterm and return results
#searchTerm: user provided input
#searchType: dropdown menu selection
def keywordSearch(searchTerm, searchType):
    #which collection to hit
    querySet = []
    #search set collection
    if searchType == "set":
        keyTermPair = searchTerm.split("=")
        #perform db query based on search operator in user submited string
        if keyTermPair[0] == "code":
            querySet = mtgSet.objects.filter(code = keyTermPair[1])
        elif keyTermPair[0] == "block":
            querySet = mtgSet.objects.filter(block = keyTermPair[1])
        elif keyTermPair[0] == "name":
             querySet = mtgSet.objects.filter(name = keyTermPair[1])
    #search card collection
    if searchType =="card":
        keyTermPair = searchTerm.split("=")
        #perform db query based on search operator in user submited string
        if keyTermPair[0] == "keyword":
            #term exists in card name or text
            querySet = mtgCard.objects.filter(Q(keyword__contains = keyTermPair[1])| 
                    Q(text__contains = keyTermPair[1]))
        elif keyTermPair[0] == "cardType":
            #check all type fields
            querySet = mtgCard.objects.filter(
                    Q(type = keyTermPair[1])
                    | Q(types__contains = keyTermPair[1])
                    | Q(supertypes__contains = keyTermPair[1])
                    | Q(subtypes__contains = keyTermPair[1]))
        elif keyTermPair[0] == "color":
            querySet = mtgCard.objects.filter(colors__contains = keyTermPair[1])
        elif keyTermPair[0] == "artist":
            querySet = mtgCard.objects.filter(artist__contains = keyTermPair[1])
    return querySet