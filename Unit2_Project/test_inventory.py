import unittest
from inventory import *

class Test_Inventory(unittest.TestCase):
    def setUp(self):  
        self.assertRaises(TypeError, Inventory, 25, "David")
        self.assertRaises(TypeError, Inventory, "Jon", 100)
        self.assertRaises(TypeError, Inventory, 25, -2)
        self.employee1 = Inventory("John", "Black")
        self.employee2 = Inventory("Thomas", "Wayne")
        self.employee3 = Inventory("Danielle", "Dober")
        self.employee4 = Inventory("Rondo", "Ball")

    def test_overall_item_exists(self):
        self.assertTrue(Inventory.overall_item_exists("Beverages", "black coffee", "HOT"))
        self.assertFalse(Inventory.overall_item_exists("beverages", "black coffee", "Cold"))
        self.assertTrue(Inventory.overall_item_exists("sweet foods", "muffins", "BLUEBERRY"))
        self.assertFalse(Inventory.overall_item_exists("SWEET FOODS", "bagels", "jelly filled"))
        self.assertTrue(Inventory.overall_item_exists("savory FOODs", "crepes", "spinach bacon"))
        self.assertFalse(Inventory.overall_item_exists("SAVORY foods", "black coffee", "Cold"))
        self.assertFalse(Inventory.overall_item_exists("snacks", "black coffee", "Hot"))
        self.assertFalse(Inventory.overall_item_exists("beverages", "water", "Cold"))

    def test_section_valid(self):
        self.assertRaises(TypeError, Inventory.section_valid, 260.0)
        self.assertRaises(TypeError, Inventory.section_valid, -500)
        self.assertTrue(Inventory.section_valid("Beverages"))
        self.assertTrue(Inventory.section_valid("SWEET FOODS"))
        self.assertTrue(Inventory.section_valid("savory FooDs"))
        self.assertFalse(Inventory.section_valid("hot foods"))
        self.assertFalse(Inventory.section_valid("cold Foods"))

    def test_category_valid(self):
        self.assertRaises(TypeError, Inventory.category_valid, "beverges", 35)
        self.assertRaises(TypeError, Inventory.category_valid, 600, "muffins")
        self.assertTrue(Inventory.category_valid("Beverages", "black coffee"))
        self.assertTrue(Inventory.category_valid("SWEET FOODS", "CHEESEcakes"))
        self.assertTrue(Inventory.category_valid("savory FooDs", "omlettes"))
        self.assertFalse(Inventory.category_valid("SWEET foods", "crepes"))
        self.assertFalse(Inventory.category_valid("beverages", "water"))


    def test_item_valid(self):
        self.assertRaises(TypeError, Inventory.item_valid, "beverages", "milkshakes", 25)
        self.assertRaises(TypeError, Inventory.item_valid, "sweet Foods", 30, "glazed")
        self.assertRaises(TypeError, Inventory.item_valid, 3.0, "omlettes", "plain")
        self.assertTrue(Inventory.item_valid("beverages", "BLACK Coffee", "with ice"))
        self.assertFalse(Inventory.item_valid("beverages", "smoothies", "orange"))
        self.assertTrue(Inventory.item_valid("Sweet Foods", "Muffins", "blueberry"))
        self.assertFalse(Inventory.item_valid("sweet foods", "donuts", "plain"))
        self.assertTrue(Inventory.item_valid("savory foods", "homemade sandwiches", "blt"))
        self.assertFalse(Inventory.item_valid("savory foods", "handmade wraps", "beef"))


    def test_get_item_count(self):
        self.assertEqual(Inventory.get_item_count("beverages", "milkshakes", "vanilla"), 0)
        self.assertEqual(Inventory.get_item_count("Sweet foods", "cookies", "chocolate chip"), 0)
        self.assertEqual(Inventory.get_item_count("savory foods", "fresh bagels", "PoppySeed"), 0)    

    def test_add_stock(self): #using object instance
        self.assertRaises(TypeError, self.employee1.add_stock, "beverages", "milkshakes", 25, 20)
        self.assertRaises(TypeError, self.employee2.add_stock, "sweet foods", 23, "glazed", "4")
        self.assertRaises(ValueError, self.employee1.add_stock, "beverages", "black coffee", "with ice", -5)

        self.employee1.add_stock("beverages", "milkshakes", "chocolate", 30)
        self.employee2.add_stock("savory foods", "omlettes", "diced onions", 25)
        self.assertEqual(Inventory.get_item_count("beverages", "milkshakes", "chocolate"), 30)
        self.assertEqual(Inventory.get_item_count("savory foods", "omlettes", "diced onions"), 25)

        #Testing update_tracker after add_stock
        self.assertEqual(len(Inventory.update_track[self.employee1.full_name]["add"]), 1)
        self.assertEqual(len(Inventory.update_track[self.employee2.full_name]["add"]), 1)

    def test_order_fulfilled(self):
        self.assertTrue(Inventory.order_fulfilled("beverages", "milkshakes", "chocolate", 10))
        self.assertTrue(Inventory.order_fulfilled("savory foods", "omlettes", "diced onions", 15))
        self.assertFalse(Inventory.order_fulfilled("sweet foods", "muffins", "chocolate milk", 10))
        self.assertFalse(Inventory.order_fulfilled("beverages", "smoothies", "mango-pineapple", 6))

    def test_remove_stock(self): #using object instance
        self.assertRaises(TypeError, self.employee3.remove_stock, "beverages", "milkshakes", 25, 20)
        self.assertRaises(TypeError, self.employee4.remove_stock, "sweet foods", 23, "glazed", "4")
        self.assertRaises(ValueError, self.employee4.remove_stock, "beverages", "black coffee", "with ice", -5)

        self.assertEqual(self.employee3.remove_stock("beverages", "milkshakes", "chocolate", 10), "chocolate has been decremented by 10")
        self.assertEqual(self.employee4.remove_stock("savory foods", "omlettes", "diced onions", 15), "diced onions has been decremented by 15")
        self.assertEqual(self.employee3.remove_stock("beverages", "milkshakes", "vanilla", 5), "There is not enough vanilla to decrement")
        self.assertEqual(Inventory.get_item_count("beverages", "milkshakes", "chocolate"), 20)
        self.assertEqual(Inventory.get_item_count("savory foods", "omlettes", "diced onions"), 10)

        #Testing update_tracker after remove_stock
        self.assertEqual(len(Inventory.update_track[self.employee3.full_name]["remove"]), 1)
        self.assertEqual(len(Inventory.update_track[self.employee4.full_name]["remove"]), 1)

if __name__ == "__main__":
    unittest.main()

