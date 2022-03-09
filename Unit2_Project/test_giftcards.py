from giftcards import *
import unittest

class Test_Giftcard(unittest.TestCase):
    def setUp(self):
        self.giftcard1 = Giftcard()
        self.giftcard2 = Giftcard()
        self.giftcard3 = Giftcard()
    
    def test_generate_code(self):
        self.assertIn(self.giftcard1.gift_code, Giftcard.generated_giftcards)
    
    def test_authenticate(self):
        self.assertEqual(Giftcard().authenticate(self.giftcard1.gift_code), True)
        self.assertRaises(TypeError, Giftcard().authenticate, 123645)
    
    def test_redeem(self):
        Giftcard().redeem(self.giftcard1.gift_code)
        self.assertEqual(self.giftcard1.redeem_state, True)

    def test_set_trivia_answer(self):
        Giftcard.set_trivia_solution("orange")
        self.assertEqual(Giftcard.trivia_solution, "orange")