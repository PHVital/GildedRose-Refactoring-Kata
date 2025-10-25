# -*- coding: utf-8 -*-

from updater import AgedBrieUpdater, SulfurasUpdater, BackstagePassesUpdater, ConjuredUpdater, ItemUpdater # noqa


class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.updater_strategies = {
            "Aged Brie": AgedBrieUpdater,
            "Sulfuras, Hand of Ragnaros": SulfurasUpdater,
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassesUpdater, # noqa
            "Conjured Mana Cake": ConjuredUpdater
        }

    def update_quality(self):
        for item in self.items:
            UpdaterClass = self.updater_strategies.get(item.name, ItemUpdater)

            updater = UpdaterClass(item)

            updater.update_sell_in()
            updater.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
