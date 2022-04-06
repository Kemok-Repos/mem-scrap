import sys
import pandas as pd

URI = 'https://mem.gob.gt/que-hacemos/hidrocarburos/comercializacion-downstream/precios-combustible-nacionales/'

gas_price_table = pd.read_html(URI)[0]

gas_price_table = gas_price_table.drop(gas_price_table.columns[[1, 3]], axis=1)

last_week = gas_price_table.columns[1]
last_week_curated = last_week.split(': ', 1)[1].replace('de', '')

gas_price_table.rename(columns={last_week : last_week_curated}, inplace=True)

print(gas_price_table)
