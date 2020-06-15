from django.db import models

# Create your models here.

class mtgCardManager(models.Manager):
    def create_card(self, json):
        mtgcard = self.create(**json)
        return mtgcard

class mtgCard(models.Model):
    name = models.CharField(max_length = 200, default=None, blank=True, null=False)
    mana_cost = models.CharField(max_length = 200, default=None, blank=True, null=True)
    cmc = models.TextField(default=None, blank=True, null=True)
    colors = models.TextField(default=None, blank=True, null=True)
    types = models.TextField(default=None, blank=True, null=True)
    rarity = models.CharField(max_length = 200, default=None, blank=True, null=True)
    text = models.TextField(default=None, blank=True, null=True)
    power = models.CharField(max_length = 200, default=None, blank=True, null=True)
    toughness = models.CharField(max_length = 200, default=None, blank=True, null=True)
    set_name = models.CharField(max_length = 200, default=None, blank=True, null=True)
    legalities = models.TextField(default=None, blank=True, null=True)
    rulings = models.TextField(default=None, blank=True, null=True)
    layout = models.CharField(max_length = 200, default=None, blank=True, null=True)
    color_identity = models.TextField(default=None, blank=True, null=True)
    names = models.CharField(max_length = 200, default=None, blank=True, null=True)
    type = models.CharField(max_length = 200, default=None, blank=True, null=True)
    supertypes = models.TextField(default=None, blank=True, null=True)
    subtypes = models.TextField(default=None, blank=True, null=True)
    flavor= models.CharField(max_length = 200, default=None, blank=True, null=True)
    artist = models.CharField(max_length = 200, default=None, blank=True, null=True)
    number = models.CharField(max_length = 200, default=None, blank=True, null=True)
    loyalty = models.CharField(max_length = 200, default=None, blank=True, null=True)
    multiverse_id = models.TextField(default=None, blank=True, null=True)
    variations = models.CharField(max_length = 200, default=None, blank=True, null=True)
    watermark = models.CharField(max_length = 200,default=None, blank=True, null=True)
    border = models.CharField(max_length = 200, default=None, blank=True, null=True)
    timeshifted = models.CharField(max_length = 200, default=None, blank=True, null=True)
    hand = models.CharField(max_length = 200, default=None, blank=True, null=True)
    life = models.CharField(max_length = 200, default=None, blank=True, null=True)
    release_date = models.CharField(max_length = 200, default=None, blank=True, null=True)
    starter = models.CharField(max_length = 200, default=None, blank=True, null=True)
    printings = models.TextField(default=None, blank=True, null=True)
    original_text = models.TextField(default=None, blank=True, null=True)
    original_type = models.CharField(max_length = 200, default=None, blank=True, null=True)
    source = models.CharField(max_length = 200,default=None, blank=True, null=True)
    image_url = models.URLField(max_length=200,default=None, blank=True, null=True)
    set = models.CharField(max_length = 200, default=None, blank=True, null=True)
    id = models.CharField(max_length = 200,primary_key=True)
    foreign_names = models.TextField(default=None, blank=True, null=True)


    objects=mtgCardManager()


class mtgSetManager(models.Manager):
    def create_set(self, json):
        mtgset = self.create(**json)
        return mtgset

class mtgSet(models.Model):
    code = models.CharField(max_length = 200, default=None, blank=True, null=True)
    name = models.CharField(max_length = 200, default=None, blank=True, null=True)
    gatherer_code = models.CharField(max_length = 200, default=None, blank=True, null=True)
    old_code = models.CharField(max_length = 200, default=None, blank=True, null=True)
    magic_cards_info_code = models.CharField(max_length = 200, default=None, blank=True, null=True)
    release_date = models.CharField(max_length = 200, default=None, blank=True, null=True)
    border = models.CharField(max_length = 200, default=None, blank=True, null=True)
    type = models.CharField(max_length = 200, default=None, blank=True, null=True)
    block = models.CharField(max_length = 200, default=None, blank=True, null=True)
    online_only = models.CharField(max_length = 200, default=None, blank=True, null=True)
    booster = models.TextField(default=None, blank=True, null=True)
    mkm_id = models.TextField(default=None, blank=True, null=True)
    mkm_name = models.CharField(max_length = 200, default=None, blank=True, null=True)

    objects=mtgSetManager()