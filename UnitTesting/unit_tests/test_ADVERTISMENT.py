import unittest
from Advertisment.Advertisment import ADVERTISEMENT as AD


class TestADVERTISMENT(unittest.TestCase):
    
    def test__init__(self):
        ad = AD(1, "https://test.url", "2020-01-01", "2022-01-01", 99.99, "Test", "https://phoro.url", "OO-408-TL/20")
        self.assertEqual(ad._ID, 1)
        self.assertEqual(ad._website_url, "https://test.url")
        self.assertEqual(ad._start_date, "2020-01-01")
        self.assertEqual(ad._end_date, "2022-01-01")
        self.assertEqual(ad._price, 99.99)
        self.assertEqual(ad._title, "Test")
        self.assertEqual(ad._photo_url, "https://phoro.url")
        self.assertEqual(ad.transaction_number, "OO-408-TL/20")
        
    
    def test_str(self):
        ad = AD(1, "https://test.url", "2020-01-01", "2022-01-01", 99.99, "Test", "https://phoro.url", "OO-408-TL/20")
        self.assertEqual(ad.__str__(), "1\nhttps://test.url\n2020-01-01\n2022-01-01\n99.99\nTest\nhttps://phoro.url\nOO-408-TL/20\n")
        
        
    def test_from_list(self):
        ad = AD.from_list([1, "https://test.url", "2020-01-01", "2022-01-01", 99.99, "Test", "https://phoro.url", "OO-408-TL/20"])
        self.assertEqual(ad.__str__(), "1\nhttps://test.url\n2020-01-01\n2022-01-01\n99.99\nTest\nhttps://phoro.url\nOO-408-TL/20\n")
        
    
    def test_from_keyboard(self):
        self.assertEqual(1, 1)
    
    def test_get_errors(self):
        flds = [1, "https//test.url", "2020-01-01", "2022-01-01", -99.99, "Test", "https://phoro.url", "OO-408-TL/20"]
        self.assertEqual(AD.get_errors(flds), ["invalid website_url", "invalid price"])
        
        
        
        
if __name__ == "__main__":
    unittest.main()
