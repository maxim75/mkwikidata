import unittest
import  mkwikidata

class TestStringMethods(unittest.TestCase):

    def test_get_wd_id_from_url(self):
        self.assertEqual(mkwikidata.get_id_from_url("http://www.wikidata.org/entity/Q44"), 'Q44')
        self.assertEqual(mkwikidata.get_id_from_url("https://commons.wikimedia.org/entity/M81321868"), 'M81321868')

    def test_get_wd_id_from_url(self):
        self.assertEqual(mkwikidata.get_int_id_from_url("http://www.wikidata.org/entity/Q44"), 44)
        self.assertEqual(mkwikidata.get_int_id_from_url("https://commons.wikimedia.org/entity/M81321868"), 81321868)

    # def test_ss(self):
    #     self.assertEqual(2, 44)

if __name__ == '__main__':
    unittest.main()