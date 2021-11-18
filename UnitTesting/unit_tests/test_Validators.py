import unittest
from Validators.Validator import Validators as V

class TestValidators(unittest.TestCase):
    
    
    
    def test_isInt(self):
        self.assertEqual(V.isInt(1), True)
        self.assertEqual(V.isInt("Hello"), False)
        
    def test_isPositive(self):
        self.assertEqual(V.isPositive(1), True)
        self.assertEqual(V.isPositive(-10), False)
        self.assertEqual(V.isPositive("Hello"), False)
        
    def test_a_bigger_b(self):
        self.assertEqual(V.a_bigger_b(0, 1), False)
        self.assertEqual(V.a_bigger_b(-2, -1), False)
        self.assertEqual(V.a_bigger_b("Hello", -1), "Value should be number")
    
    def test_Exit(self):
        self.assertEqual(V.Exit("Hello"), None)
        
    def test_wrong_date(self):
        self.assertRaises(ValueError, V.wrong_date, "2022-01-01", "2020-02-02")
        
    def test_ID(self):
        @V.ID
        def test(self, ID):
            pass
        
        self.assertRaises(ValueError, test, self, -9)
        self.assertRaises(ValueError, test, self, "Hello")
        
        
    def test_url(self):
        @V.url
        def test(self, ID):
            pass
        
        self.assertRaises(ValueError, test, self, "https://hello.")
        self.assertRaises(ValueError, test, self, 1)
        
    
    def test_date(self):
        @V.date
        def test(self, ID):
            pass
        
        self.assertRaises(ValueError, test, self, "2021-02-31")
        self.assertRaises(ValueError, test, self, 31)
        
        
    def test_currency(self):
        @V.currency
        def test(self, ID):
            pass
        
        self.assertRaises(ValueError, test, self, -9)
        self.assertRaises(ValueError, test, self, "Hello")
        
        
    def test_transaction_number(self):
        @V.transaction_number
        def test(self, ID):
            pass
        
        self.assertRaises(ValueError, test, self, "oi-19-oi/32")
        self.assertRaises(ValueError, test, self, 1)
        
        
    def test_title(self):
        @V.title
        def test(self, ID):
            pass
        
        self.assertRaises(ValueError, test, self, "title")
        self.assertRaises(ValueError, test, self, "Tit1e")
        self.assertRaises(ValueError, test, self, "1")
        self.assertRaises(ValueError, test, self, 1)
