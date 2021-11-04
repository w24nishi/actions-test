import glob
import json
import logging
import os
import requests

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def local_files():
    locals = glob.glob('visualizer/*.json')
    logger.info(locals)
    return locals

def get_something():
    res = requests.get(
        'https://www.google.com'
    )
    logger.info(res.json())

if __name__ == '__main__':
    logger.info(os.environ.get('HOGEFUGA'))
    files = local_files()
    for file in files:
        with open(file) as f:
            logger.info(json.load(f))
    get_something()
