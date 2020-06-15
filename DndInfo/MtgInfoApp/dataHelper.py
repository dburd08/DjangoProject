import requests
import json
from mtgsdk import *
from .models import mtgCard, mtgSet


#get spell data from dnd5e api
def spellsDataRequest():
    r = requests.get('https://www.dnd5eapi.co/api/spells')
    responseJson = r.json()
    results=responseJson["results"]
    print(results)

#get monsters from dnd5e api
def monstersDataRequest():
    r = requests.get('https://www.dnd5eapi.com/api/monsters')
    responseJson = r.json()
    results=responseJson["results"]

#get cards from MTG api
def magicCardsDataRequest():
    #get all cards
    #cards = Card.where(set='thb').all()
    #get smaller set of cards
    cardsSmaller = Card.where(page=5).where(pageSize=50).all()
    addCardsToDatabase(cardsSmaller)
    return cardsSmaller

#loop from collection of cards and convert into Model object for db storage
def addCardsToDatabase(cards):
    for x in cards:
        slimCard = x.__dict__
        del slimCard['foreign_names']
        mtgCard.objects.create_card(slimCard)

#get magic sets from MTG api
def magicSetsDataRequest():
    sets = Set.all()
    addSetsToDatabase(sets)

#loop from collection of sets and convert into Model object for db storage
def addSetsToDatabase(sets):
    for x in sets:
        print(x.__dict__)
        mtgSet.objects.create_set(x.__dict__)


