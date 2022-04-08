

# Función para devolver el nùmero correspondiente al mes
def mesANumero(string):
   
    meses = {
        'enero': "01",
        'febrero': "02",
        'marzo': "03",
        'abril': "04",
        'mayo': "05",
        'junio': "06",
        'julio': "07",
        'agosto': "08",
        'septiembre': "09",
        'octubre': "10",
        'noviembre': "11",
        'diciembre': "12"
        }

    fecha = string.split("  ")
    dia =  fecha[0]
    mes =  fecha[1]
    anio = fecha[2]

    try:
        nro_mes = str(meses[mes.lower()])
        return dia + "/" +  nro_mes + "/" + anio
    except:
        raise ValueError('No es un mes')

