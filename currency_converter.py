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
convert_metavar = ('AMOUNT', 'CURRENCY_FROM', 'CURRENCY_TO')
date_metavar = ('YEAR', 'MONTH', 'DAY')
arg_parser.add_argument('-d', '--date', help=helps['date'], nargs=3, metavar=date_metavar)
arg_parser.add_argument('-b', '--base', help=helps['base'], metavar='CURRENCY')
arg_parser.add_argument('-s', '--show', help=helps['show'], nargs='+', metavar='CURRENCY')
arg_parser.add_argument('-c', '--convert', help=helps['convert'], nargs=3, metavar=convert_metavar)
args = arg_parser.parse_args()

# requests the rates on given date
date = 'latest'
url = 'http://api.fixer.io/'
url_params = ''
if (args.date):
  month = args.date[1].zfill(2)
  day = args.date[2].zfill(2)
  date = args.date[0] + '-' + month + '-' + day

url += date

# changes base currency
if (args.base):
  url_params += 'base=' + args.base
else:
  url_params += 'base=USD'

# only shows specified currencies
if (args.show):
  currencies_to_show = args.show
  url_params += '&symbols=' + currencies_to_show[0]
  for cur in currencies_to_show[1:]:
    url_params += ',' + cur

# forms the final url for api call
url += '?' + url_params

# api call and convert json to python objects
request = requests.get(url)
rates_json = request.json()
rates_json_string = json.dumps(rates_json)
rates = json.loads(rates_json_string)

# prints date of the rate
print 'Date of Rates: ' + rates['date'] + '\n'

# prints currency base and amount
print rates['base'] + ': 1'
print '---------------------------'

# prints the rates
for cur, rate in rates['rates'].iteritems():
  print cur + ': ' + str(rate)
