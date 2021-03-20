############
mkwikidata
############

Run SPARQL queries on Wikidata or other services

.. code:: python

        query = """
            SELECT ?unicode_charater
            WHERE 
            {
                wd:$id wdt:P487 ?unicode_charater.
            }
        """
        result = mkwikidata.run_query(query, params={ "id": "Q44" }) 
        result # 🍺