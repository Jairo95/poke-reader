"""Programa de ejemplo siguiendo la guia de estilos de PEP 8

"""


__version__ = '0.1'
__author__ = 'Jairo'


import datetime
import traceback

import requests
import serializers
import utils


URL = 'https://pokeapi.co/api/v2/type/{pk}/'
AMOUNT = 10


def download_object(url, params=None, object_type=None):
    try:
        data = requests.get(url=url, params=params).json()
        return utils.deserialize_json(object_type, data)
    except Exception as e:
        traceback.print_exc()
        return None


def main():
    """ Descarga los tipos de pokemon

    """

    for pk in range(AMOUNT):
        type_ = download_object(URL.format(pk=pk + 1), object_type=serializers.Type)
        if type_ is None:
            print('NONE response')
            continue
        print('{}'.format(datetime.datetime.now()))
        print('[TYPE]:', str(type_))


if __name__ == '__main__':
    main()
