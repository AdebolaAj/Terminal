from giftcards import *
import unittest

class Test_Giftcard(unittest.TestCase):
    def setUp(self):
        self.assertRaises(TypeError, Giftcard, "abcd-efgh", 2500, False)
        self.assertRaises(TypeError, Giftcard, ["abcd-efgh"], "Free dinner", True)
        self.assertRaises(TypeError, Giftcard, "abcd-efgh", "Free beverage", 1)

        self.card1 = Giftcard("K1u0-h0vN-1RnQ", "10% off a savory item")
        self.card2 = Giftcard("O5g8-n9lS-2JlP", "Free Sunday brunch combo for 2")
        self.card3 = Giftcard("M5u9-j8bS-6TdM", "1 free Thursday lunch combo", True)

    def test_generate_and_authenticate(self):
        a = Giftcard.generate_code()
        b = Giftcard.generate_code()
        self.assertTrue(Giftcard.authenticate(a))
        self.assertTrue(Giftcard.authenticate(b))
        self.assertFalse(Giftcard.authenticate("abcd-efgh-ijkl"))
        self.assertFalse(Giftcard.authenticate("1234-5678-9112"))

    def test_redeem(self):
        self.assertEqual(self.card1.redeem(), "10% off a savory item")
        self.assertEqual(self.card2.redeem(), "Free Sunday brunch combo for 2")
        self.assertEqual(self.card3.redeem(), None)

    def test_to_document(self):
        self.assertEqual(self.card1.to_document(), {"giftcode": self.card1.gift_code, "gift_value": self.card1.gift_value, "redeem_state": self.card1.redeem_state})
        self.assertEqual(self.card3.to_document(), {"giftcode": self.card3.gift_code, "gift_value": self.card3.gift_value, "redeem_state": self.card3.redeem_state})

    def test_from_document(self):
        self.assertRaises(TypeError, Giftcard.from_document, {"apple"})
        self.assertRaises(TypeError, Giftcard.from_document, ["banana"])
        self.assertRaises(TypeError, Giftcard.from_document, "orange")
        a = {"giftcode": "B6x3-y8xG-4TjN", "gift_value": "20% off any total order", "redeem_state": False}
        self.assertEqual(Giftcard.from_document(a).gift_code, "B6x3-y8xG-4TjN")
        self.assertEqual(Giftcard.from_document(a).gift_value, "20% off any total order")
        self.assertEqual(Giftcard.from_document(a).redeem_state, False)

    def test_create_new(self):
        a = Giftcard.create_new()
        self.assertTrue(a.gift_code)
    
if __name__ == "__main__":
    unittest.main()