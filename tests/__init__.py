import unittest
import  mkwikidata

class TestStringMethods(unittest.TestCase):

    def test_get_wd_id_from_url(self):
        self.assertEqual(mkwikidata.get_id_from_url("http://www.wikidata.org/entity/Q44"), 'Q44')
        self.assertEqual(mkwikidata.get_id_from_url("https://commons.wikimedia.org/entity/M81321868"), 'M81321868')

    def test_get_int_id_from_url(self):
        self.assertEqual(mkwikidata.get_int_id_from_url("http://www.wikidata.org/entity/Q44"), 44)
        self.assertEqual(mkwikidata.get_int_id_from_url("https://commons.wikimedia.org/entity/M81321868"), 81321868)

    def test_get_coordinates_from_wd_point(self):
        (lat, lng) = mkwikidata.get_coordinates_from_wd_point("Point(151.02 -34.01)")
        self.assertEqual(lat, -34.01)
        self.assertEqual(lng, 151.02)

    def test_run_query(self):

        # get unicode character for beer
        query = """
            SELECT ?unicode_charater
            WHERE 
            {
            wd:Q44 wdt:P487 ?unicode_charater.
            }
        """
        result = mkwikidata.run_query(query)
        self.assertEqual(result["results"]["bindings"][0]["unicode_charater"]["value"], "🍺")
if __name__ == '__main__':
    unittest.main()