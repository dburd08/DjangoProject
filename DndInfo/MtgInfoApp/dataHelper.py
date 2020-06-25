import requests
import json
from mtgsdk import Card, Set
from .models import mtgCard, mtgSet


#get cards from MTG api
def magicCardsDataRequest():
    #get smaller set of cards
    cardsSmaller = Card.where(page=8).where(pageSize=100).all()
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
        mtgSet.objects.create_set(x.__dict__)


