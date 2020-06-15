from django.shortcuts import render
from django.http import HttpResponse
from .dataHelper import magicCardsDataRequest, magicSetsDataRequest
from django.db.models import Q
from .models import *
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
    # resultsList=[]
    # for sr in searchResults:
    #     resultsList.append(sr)
    dynamicData = {'data':searchResults}
    return render(request,'search.html', context=dynamicData)


#app landing page, contains input field for search
def home(request):
    return render(request, 'home.html')


#query the database for searchterm and return results
def keywordSearch(searchTerm, searchType):
    #which collection to hit
    print (mtgSet.objects.all())
    querySet = []
    if searchType == "set":
        #search set collection
        keyTermPair = searchTerm.split("=")
        #perform db query based on search operator in user submited string
        if keyTermPair[0] == "code":
            querySet = mtgSet.objects.filter(code = keyTermPair[1])
        elif keyTermPair[0] == "block":
            querySet = mtgSet.objects.filter(block = keyTermPair[1])
        elif keyTermPair[0] == "name":
             querySet = mtgSet.objects.filter(name = keyTermPair[1])
    if searchType =="card":
        #search card collection
        keyTermPair = searchTerm.split("=")
        #perform db query based on search operator in user submited string
        if keyTermPair[0] == "keyword":
            #term exists in card name or text
            querySet = mtgCard.objects.filter(Q(keyword__contains = keyTermPair[1])
                                            | Q(text__contains = keyTermPair[1]))
        elif keyTermPair[0] == "cardType":
            #check all type fields
            querySet = mtgCard.objects.filter(Q(type = keyTermPair[1]) | Q(types__contains = keyTermPair[1])
                                            | Q(supertypes__contains = keyTermPair[1]) | Q(subtypes__contains = keyTermPair[1]))
        elif keyTermPair[0] == "color":
            querySet = mtgCard.objects.filter(colors__contains = keyTermPair[1])
        elif keyTermPair[0] == "artist":
            querySet = mtgCard.objects.filter(artist__contains = keyTermPair[1])
    for q in querySet:
        print(q)
    return querySet