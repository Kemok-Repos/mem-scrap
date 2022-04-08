import psycopg2
from datetime import datetime

def connect():
    #Conexion 
    conexion = psycopg2.connect(dbname='data_publica', host='45.56.117.5', user='dataadmin', password='$q%$=0#WyCI1.')
    return (conexion)

# Objeto conexión
conexion = connect()

def consultar(fecha):  

    # Verifico que no existan los precios para la fecha
    consulta = "SELECT COUNT(*) FROM precio_gasolina_mem WHERE fecha = '" + str(datetime.strptime(fecha, '%d/%m/%Y')) + "'"

    cur = conexion.cursor()
    cur.execute(consulta)
    conexion.commit()

    resultado= cur.fetchone()[0]
    return resultado
    cur.close()

def agregar(lProductos, lPrecios, fecha):

    # Verifico que no existan los precios para la fecha
    resultado = consultar(fecha) 

    if resultado==0:
        agregar=''
        # Recorro las listas y armo las sentencias insert
        for i in range(0,len(lProductos)):
            agregar +=  "INSERT INTO precio_gasolina_mem (fecha,producto,precio,fecha_actualizado) " 
            agregar +=  "VALUES ('"+ str(datetime.strptime(fecha, '%d/%m/%Y')) +"', '" + lProductos[i] + "'," + str(lPrecios[i])+",'"+ str(datetime.today().strftime('%Y-%m-%d %H:%M')) +"');"
        
        cur = conexion.cursor()
        cur.execute(agregar)
        conexion.commit()
        cur.close()
        conexion.close()
