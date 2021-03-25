import unittest
import mkwikidata


class TestStringMethods(unittest.TestCase):

    def test_get_wd_id_from_url(self):
        self.assertEqual(mkwikidata.get_id_from_url(
            "http://www.wikidata.org/entity/Q44"), 'Q44')
        self.assertEqual(mkwikidata.get_id_from_url(
            "https://commons.wikimedia.org/entity/M81321868"), 'M81321868')

    def test_get_int_id_from_url(self):
        self.assertEqual(mkwikidata.get_int_id_from_url(
            "http://www.wikidata.org/entity/Q44"), 44)
        self.assertEqual(mkwikidata.get_int_id_from_url(
            "https://commons.wikimedia.org/entity/M81321868"), 81321868)

    def test_get_coordinates_south_east_from_wd_point(self):
        (lat, lng) = mkwikidata.get_coordinates_from_wd_point(
            "Point(151.02 -34.01)")
        self.assertEqual(lat, -34.01)
        self.assertEqual(lng, 151.02)

    def test_get_coordinates_north_west_from_wd_point(self):
        (lat, lng) = mkwikidata.get_coordinates_from_wd_point(
            "Point(-10.01 40.04)")
        self.assertEqual(lat, 40.04)
        self.assertEqual(lng, -10.01)

    def test_run_query(self):

        # get unicode character for beer
        query = """
            SELECT ?unicode_charater
            WHERE 
            {
                wd:$id wdt:P487 ?unicode_charater.
            }
        """
        result = mkwikidata.run_query(query, params={"id": "Q44"})
        self.assertEqual(result["results"]["bindings"]
                         [0]["unicode_charater"]["value"], "🍺")

    def test_convert_response_for_data_frame(self):
        test_query_result = {'head': {'vars': ['unicode_charater', 'optional_field']}, 'results': {
            'bindings': [{'unicode_charater': {'type': 'literal', 'value': '🍺'}}]}}

        (result, columns) = mkwikidata.convert_response_for_data_frame(test_query_result)

        self.assertEqual(len(columns), 2)
        self.assertEqual(columns[0], "unicode_charater")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], "🍺")

if __name__ == '__main__':
    unittest.main()
