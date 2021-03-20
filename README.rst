############
mkwikidata
############

Run SPARQL queries on Wikidata or other services

.. code:: python

        query = """
            SELECT ?unicode_charater
            WHERE 
            {
            wd:Q44 wdt:P487 ?unicode_charater.
            }
        """
        result = mkwikidata.run_query(query)
        result["results"]["bindings"][0]["unicode_charater"]["value"] # "🍺"