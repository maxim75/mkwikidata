"""Utility functions for working with Wikidata"""
import requests
import re
from string import Template

__version__ = '0.14'


def get_coordinates_from_wd_point(point_str):
    regex = re.compile("Point\((-?[\d\.]+) (-?[\d\.]+)\)")
    match = regex.match(point_str)
    if match is None:
        return None
    return float(match.groups()[1]), float(match.groups()[0])


def get_id_from_url(url):
    regex = re.compile("https?:\/\/.*/entity\/([A-Z]\d+)")
    match = regex.match(url)
    if match is None:
        return None
    return match.groups()[0]


def get_int_id_from_url(url):
    result = get_id_from_url(url)
    if result is None:
        return None
    value_str = re.sub(r"[A-Z]", "", result)
    return int(value_str)


def run_query(query, params={}, service_url=None):

    if service_url is None:
        service_url = 'https://query.wikidata.org/sparql'

    query_template = Template(query)
    execute_query = query_template.substitute(**params)
    r = requests.post(service_url, params={'format': 'json', 'query': execute_query})
    response_json = r.json()
    return response_json


def convert_response_for_data_frame(query_result):
    columns = query_result["head"]["vars"]
    result = []
    for row in query_result["results"]["bindings"]:
        column_values = []
        for column in columns:
            if column in row:
                column_values.append(row[column]["value"])
            else:
                column_values.append(None)
        result.append(column_values)

    return (result, columns)

""" Returns columns and values fot pandas DataFrame"""
def run_query_for_dataframe(query, params={}, service_url=None):
    query_result = run_query(query, params=params, service_url=service_url)
    return convert_response_for_data_frame(query_result)
    