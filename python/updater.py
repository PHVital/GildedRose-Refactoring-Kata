class ItemUpdater:
    def __init__(self, item):
        self.item = item

    def update_sell_in(self):
        self.item.sell_in -= 1

    def update_quality(self):
        if self.item.quality > 0:
            self.item.quality -= 1
        if self.item.sell_in < 0:
            if self.item.quality > 0:
                self.item.quality -= 1


class AgedBrieUpdater(ItemUpdater):
    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1

        if self.item.sell_in < 0:
            if self.item.quality < 50:
                self.item.quality += 1


class SulfurasUpdater(ItemUpdater):
    def update_quality(self):
        pass

    def update_sell_in(self):
        pass


class BackstagePassesUpdater(ItemUpdater):
    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1

            if self.item.sell_in < 10:
                if self.item.quality < 50:
                    self.item.quality += 1

            if self.item.sell_in < 5:
                if self.item.quality < 50:
                    self.item.quality += 1

        if self.item.sell_in < 0:
            self.item.quality = 0

        if self.item.quality > 50:
            self.item.quality = 50


class ConjuredUpdater(ItemUpdater):
    def update_quality(self):
        if self.item.quality > 0:
            self.item.quality -= 2
        if self.item.sell_in < 0:
            if self.item.quality > 0:
                self.item.quality -= 2

        if self.item.quality < 0:
            self.item.quality = 0
