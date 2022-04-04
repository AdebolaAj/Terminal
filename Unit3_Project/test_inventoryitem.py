import unittest
from inventoryitem import *

'''
   @classmethod
    def from_document(cls, document):
        return InventoryItem(document['section'], document['category'], document['item'], document['amount'])
'''

class Test_InventoryItem(unittest.TestCase):
    

    def setUp(self):

        #tests for type and value errors
        self.assertRaises(TypeError, InventoryItem, 5, 'black coffee', 'with ice', 5)
        self.assertRaises(TypeError, InventoryItem, 'beverages', True, 'with ice', 5)
        self.assertRaises(TypeError, InventoryItem, 'savory foods', 'handmade wraps', 10, 5)
        self.assertRaises(TypeError, InventoryItem, 'savory foods', 'handmade wraps', 'chicken', '5')
        self.assertRaises(ValueError, InventoryItem, 'savory foods', 'handmade wraps', 'chicken', -5)

        #creating instances of the class to use in testing 
        self.item1 = InventoryItem("beverages", 'black coffee', 'with ice', 60)
        self.item2 = InventoryItem("sweet foods", 'donuts', 'glazed', 35)
        self.item3 = InventoryItem("savory foods", 'fresh bagels', 'plain', 45)

    def test_CanRemoveAmount(self):

        #tests for type and value errors
        self.assertRaises(TypeError, self.item1.CanRemoveAmount, '10')
        self.assertRaises(TypeError, self.item1.CanRemoveAmount, 2.5)
        self.assertRaises(ValueError, self.item2.CanRemoveAmount, 0)
        self.assertRaises(ValueError, self.item3.CanRemoveAmount, -6)

        #tests to ensure method works properly
        self.assertTrue(self.item1.CanRemoveAmount(10))
        self.assertTrue(self.item2.CanRemoveAmount(35))
        self.assertTrue(self.item3.CanRemoveAmount(44))
        self.assertFalse(self.item1.CanRemoveAmount(100))
        self.assertFalse(self.item2.CanRemoveAmount(36))
        self.assertFalse(self.item3.CanRemoveAmount(60))

    def test_RemoveAmount(self):

        #tests for type and value errors
        self.assertRaises(TypeError, self.item1.RemoveAmount,'10')
        self.assertRaises(TypeError, self.item2.RemoveAmount, 10.5)
        self.assertRaises(ValueError, self.item3.RemoveAmount, -5)
        self.assertRaises(ValueError, self.item1.RemoveAmount, 0)

        #calling method on instances 
        self.item1.RemoveAmount(5)
        self.item2.RemoveAmount(20)
        self.item3.RemoveAmount(45)

        #tests to ensure method works properly
        self.assertEqual(self.item1.amount, 55)        
        self.assertEqual(self.item2.amount, 15)
        self.assertEqual(self.item3.amount, 0)

    def test_AddAmount(self):

        #tests for type and value errors
        self.assertRaises(TypeError, self.item1.AddAmount, '5')
        self.assertRaises(TypeError, self.item1.AddAmount, 2.5)
        self.assertRaises(ValueError, self.item3.AddAmount, -1)
        self.assertRaises(ValueError, self.item1.AddAmount, 0)

        #calling method on instances
        self.item1.AddAmount(5)
        self.item2.AddAmount(20)
        self.item3.AddAmount(45)

        #tests to ensure method works properly
        self.assertEqual(self.item1.amount, 65)        
        self.assertEqual(self.item2.amount, 55)
        self.assertEqual(self.item3.amount, 90)

    def test_to_document(self):

        #tests to ensure method works properly
        self.assertEqual(self.item1.to_document(), {'section': 'beverages', 'category': 'black coffee', 'item': 'with ice', 'amount': 60})
        self.assertEqual(self.item2.to_document(), {'section': 'sweet foods', 'category': 'donuts', 'item': 'glazed', 'amount': 35})   
        self.assertEqual(self.item3.to_document(), {'section': 'savory foods', 'category': 'fresh bagels', 'item': 'plain', 'amount': 45})     

    def test_from_document(self):

        #tests for type and value errors
        self.assertRaises(TypeError, InventoryItem.from_document, ["beverages", 'black coffee', 'with ice', 60])
        self.assertRaises(KeyError, InventoryItem.from_document, {'first item': 'savory foods', 'category': 'fresh bagels', 'item': 'plain', 'amount': 45})
        self.assertRaises(KeyError, InventoryItem.from_document, {'section': 'savory foods', 'second layer': 'fresh bagels', 'item': 'plain', 'amount': 45})
        self.assertRaises(KeyError, InventoryItem.from_document, {'section': 'savory foods', 'category': 'fresh bagels', 5 : 'plain', 'amount': 45})
        self.assertRaises(KeyError, InventoryItem.from_document, {'section': 'savory foods', 'category': 'fresh bagels', 'item' : 'plain', 'total': 45})

        #tests to ensure method works properly
        test_document = {'_id': 'GH579h3mlji5', 'section': 'savory foods', 'category': 'handmade wraps', 'item': 'chicken', 'amount': 50}
        self.assertEqual(InventoryItem.from_document(test_document).amount, 50)
        self.assertEqual(InventoryItem.from_document(test_document).section, 'savory foods')
        self.assertEqual(InventoryItem.from_document(test_document).category, 'handmade wraps')
        self.assertEqual(InventoryItem.from_document(test_document).item, 'chicken')


if __name__ == "__main__":
    unittest.main()

