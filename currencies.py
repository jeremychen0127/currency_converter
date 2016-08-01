import collections

CURRENCIES = (
  ('AUD', 'Australian Dollar'),
  ('BGN', 'Bulgarian Lev'),
  ('BRL', 'Brazilian Real'),
  ('CAD', 'Canadian Dollar'),
  ('CHF', 'Swiss Franc'),
  ('CNY', 'Chinese Yuan/Renminbi'),
  ('CZK', 'Czech Koruna'),
  ('DKK', 'Danish Krone'),
  ('EUR', 'Euro'),
  ('GBP', 'British Pound'),
  ('HKD', 'Hong Kong Dollar'),
  ('HRK', 'Croatian Kuna'),
  ('HUF', 'Hungarian Forint'),
  ('IDR', 'Indonesian Rupiah'),
  ('ILS', 'Israeli New Shekel'),
  ('INR', 'Indian Rupee'),
  ('JPY', 'Japanese Yen'),
  ('KRW', 'South-Korean Won'),
  ('MXN', 'Mexican Peso'),
  ('MYR', 'Malaysian Ringgit'),
  ('NOK', 'Norwegian Kroner'),
  ('NZD', 'New Zealand Dollar'),
  ('PHP', 'Philippine Peso'),
  ('PLN', 'Polish Zloty'),
  ('RON', 'Romanian New Lei'),
  ('RUB', 'Russian Rouble'),
  ('SEK', 'Swedish Krona'),
  ('SGD', 'Singapore Dollar'),
  ('THB', 'Thai Baht'),
  ('TRY', 'Turkish New Lira'),
  ('USD', 'US Dollar'),
  ('ZAR', 'South African Rand')
)

CURRENCIES = collections.OrderedDict(CURRENCIES)
