import sys
import pandas as pd
import utils as u
import Fdb as fdb

URI = 'https://mem.gob.gt/que-hacemos/hidrocarburos/comercializacion-downstream/precios-combustible-nacionales/'

gas_price_table = pd.read_html(URI)[0]

gas_price_table = gas_price_table.drop(gas_price_table.columns[[1, 3]], axis=1)

last_week = gas_price_table.columns[1]
last_week_curated = last_week.split(': ', 1)[1].replace('de', '')

# Convierto la Fecha al formato dd/mm/yyyy
last_week_curated = u.mesANumero(last_week_curated)

gas_price_table.rename(columns={last_week : last_week_curated}, inplace=True)

#print(gas_price_table)

# Obtengo los productos
lProductos = list(gas_price_table[gas_price_table.columns[0]].values)
# Obtengo los precios
lPrecios = list(gas_price_table[gas_price_table.columns[1]].values)

# Agrego los productos con su precio respectivo
fdb.agregar(lProductos, lPrecios, gas_price_table.columns[1])
