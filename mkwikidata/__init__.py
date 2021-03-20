"""Utility functions for working with Wikidata"""
import requests
import re

__version__ = '0.6'

def get_coordinates_from_wd_point(point_str):
    regex = re.compile("Point\(-?([\d\.]+) (-?[\d\.]+)\)")
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


def run_query(query, service_url=None):

    if service_url is None:
        service_url = 'https://query.wikidata.org/sparql'

    r = requests.get(service_url, params={'format': 'json', 'query': query})
    response_json = r.json()
    return response_json
