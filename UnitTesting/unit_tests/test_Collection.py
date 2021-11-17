import unittest
from Advertisment.Collection import Collection
from Advertisment.Advertisment import ADVERTISEMENT as AD


class TestCollection(unittest.TestCase):
    
    def test__init__(self):
        c = Collection()
        self.assertEqual(c.size, 0)
        self.assertEqual(c._lst_of_ads, [])
        
        
    def test_copy(self):
        c = Collection()
        cc = c.copy()
        self.assertEqual(c.size, cc.size)
        self.assertEqual(c._lst_of_ads, cc._lst_of_ads)
        
        
    def test_from_json(self):
        c = Collection.from_json("unit_tests/test.json")
        self.assertEqual(c._lst_of_ads[0]._ID, 102)
        self.assertEqual(c._lst_of_ads[0]._website_url, "https://6ali.us")
        self.assertEqual(c._lst_of_ads[0]._start_date, "2020-01-26")
        self.assertEqual(c._lst_of_ads[0]._end_date, "2020-12-26")
        self.assertEqual(c._lst_of_ads[0]._price, 10543.66)
        self.assertEqual(c._lst_of_ads[0]._title, "Fat")
        self.assertEqual(c._lst_of_ads[0]._photo_url, "https://6picture.png")
        self.assertEqual(c._lst_of_ads[0].transaction_number, "yG-657-Se/01")
        
        
    def test_from_list(self):
        ad = [[1022, "https://ali.us", "2020-01-20", "2020-12-23", 10543.6, "Cat", "https://picture.png", "yG-857-Se/01"]]
        c = Collection.from_list(ad)
        self.assertEqual(c._lst_of_ads[0][0], 1022)
        self.assertEqual(c._lst_of_ads[0][1], "https://ali.us")
        self.assertEqual(c._lst_of_ads[0][2], "2020-01-20")
        self.assertEqual(c._lst_of_ads[0][3], "2020-12-23")
        self.assertEqual(c._lst_of_ads[0][4], 10543.6)
        self.assertEqual(c._lst_of_ads[0][5], "Cat")
        self.assertEqual(c._lst_of_ads[0][6], "https://picture.png")
        self.assertEqual(c._lst_of_ads[0][7], "yG-857-Se/01")
        
    
    def test_astr(self):
        c = Collection.from_json("unit_tests/test.json")
        self.assertEqual(c.__str__(), "ADVERTISMENT 0:\n\n102\nhttps://6ali.us\n2020-01-26\n2020-12-26\n10543.66\nFat\nhttps://6picture.png\nyG-657-Se/01\n\n\n")#ADVERTISMENT 1:\n\n1\nhttps://test.url\n2020-01-01\n2022-01-01\n99.99\nTets\nhttps://photo.url\nOO-408-TL/20\n\n\n")
        self.assertNotEqual(c.__str__(), "ADVERTISMENT 0:\n102\nhttps://ali.us\n2020-01-20\n2020-12-23\n10543.6\nCat\nhttps://picture.png\nyG-857-Se/01\n\n\n")
        

    def test_search(self):
        c = Collection.from_json("unit_tests/test.json")
        self.assertEqual(c.search("Fa"), "ADVERTISMENT 0\nFat\n")
        self.assertEqual(c.search("https://6a"), "ADVERTISMENT 0\nhttps://6ali.us\n")
        self.assertNotEqual(c.search("Fa"), "ADVERTISMENT 0\nhttps://picture.png\n")
        self.assertRaises(LookupError, c.search, "https://al")
        
        
    def test_ads_to_dict(self):
        c = Collection.from_json("unit_tests/test.json")
        d = c.ads_to_dict()
        self.assertEqual(d, [{'_ID': 102, '_website_url': 'https://6ali.us', '_start_date': '2020-01-26', '_end_date': '2020-12-26', '_price': 10543.66, '_title': 'Fat', '_photo_url': 'https://6picture.png', 'transaction_number': 'yG-657-Se/01'}])
        
        
    def test_dump_to_json(self):
        c = Collection.from_json("unit_tests/test.json")
        ID = c._lst_of_ads[0]._ID
        c._lst_of_ads[0]._ID = 10211
        c.dump_to_json("unit_tests/test.json")
        self.assertEqual(c._lst_of_ads[0]._ID, 10211)
        c._lst_of_ads[0]._ID = ID
        c.dump_to_json("unit_tests/test.json")
        self.assertEqual(c._lst_of_ads[0]._ID, ID)
        

    def test_add_item(self):
        c = Collection.from_json("unit_tests/test.json")
        ad = AD(1, "https://test.url", "2020-01-01", "2022-01-01", 99.99, "Test", "https://phoro.url", "OO-408-TL/20")
        c.add_item(ad)

        
    def tet_delete_item(self):
        c = Collection.from_json("unit_tests/test.json")
        c.delete_item(1)
        self.assertEqual(c._lst_of_ads[0]._ID, 102)
        
        
    def test_sort(self):
        c = Collection.from_json("unit_tests/test.json")
        ad = AD(1, "https://test.url", "2020-01-01", "2022-01-01", 99.99, "Test", "https://phoro.url", "OO-408-TL/20")
        c.add_item(ad)
        c.sort("ID")
        self.assertEqual(c._lst_of_ads[0]._ID, 1)
        self.assertEqual(c._lst_of_ads[0]._title, "Test")
        
    
    
    
if __name__ == "__main__":
    unittest.main()
