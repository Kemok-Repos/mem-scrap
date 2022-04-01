"""
OBJETIVOS: 
    - Extraer los precios de la gasolina en la modalidad: Autoservicio
LIBRERIAS: Request, lxml
"""
import requests
from lxml import html

# USER AGENT PARA PROTEGERNOS DE BANEOS
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}


# URL SEMILLA
url = 'https://mem.gob.gt/que-hacemos/hidrocarburos/comercializacion-downstream/precios-combustible-nacionales/'

# REQUERIMIENTO AL SERVIDOR
respuesta = requests.get(url, headers=headers)

# PARSEO DEL ÀRBOL HTML QUE RECIBO COMO RESPUESTA CON LXML
parser = html.fromstring(respuesta.text)

precios = list()

# EXTRACCION SOLO DEL CONTINIDO DE LAS ETIQUETASS TH
ths = parser.xpath("//table[@id='tablepress-7-no-2']//th/text()")
for p, th in enumerate(ths):
    if(th.find(":")>0):      
        v = th.find(":")+2
        precios.append(th[v:])

# EXTRACCION SOLO EL CONTENIDO DE LAS ETIQUETASS TH
tds = parser.xpath("//table[@id='tablepress-7-no-2']/tbody/tr[@class='row-2 even']/td/text()")
for p, td in enumerate(tds):
    if p==1 or p==2:
        precios.append(td)

print(precios)

