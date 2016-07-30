#!/usr/bin/python

import argparse
import requests
import json

arg_parser = argparse.ArgumentParser()
helps = {}
helps['date'] = 'the date of the rates occurred'
helps['base'] = 'the base currency'
helps['show'] = 'only show specified currencies'
helps['convert'] = 'convert one currency to another'
arg_parser.add_argument('-d', '--date', help=helps['date'])
arg_parser.add_argument('-b', '--base', help=helps['base'])
arg_parser.add_argument('-s', '--show', help=helps['show'], nargs='+', metavar='CURRENCY')
arg_parser.add_argument('-c', '--convert', help=helps['convert'], nargs=2, metavar='CURRENCY')
args = arg_parser.parse_args()

request = requests.get('http://api.fixer.io/latest')
rates_json = request.json()
rates_json_string = json.dumps(rates_json)
rates = json.loads(rates_json_string)
