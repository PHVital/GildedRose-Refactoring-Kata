# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("fixme", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)
    
    def test_conjured_item_degrades_twice_as_fast(self):
        # Setup
        items = [Item("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        
        # Execução
        gilded_rose.update_quality()
        
        # Verificação
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(18, items[0].quality)

    # 3. ADICIONE ESTE OUTRO NOVO TESTE
    def test_conjured_item_degrades_twice_as_fast_after_sellin(self):
        # Setup
        items = [Item("Conjured Mana Cake", 0, 20)]
        gilded_rose = GildedRose(items)
        
        # Execução
        gilded_rose.update_quality()
        
        # Verificação
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(16, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
