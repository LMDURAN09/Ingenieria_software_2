from flask import Flask, jsonify # Contruccion de ApIS en Phyton, Convierte los datos en formato JSON para enviarlos al cliente.
import mysql.connector #Conexion a la base de datos 
from flask_cors import CORS  # Permite que el frontend acceda a la API, 

app = Flask(__name__) # Inicia la aplicacion 
CORS(app)  # Habilita CORS para permitir solicitudes desde el navegador,
#Permite solicitudes desde navegadores que corren en dominios distintos al del backend.

port = 3000

# Configuración de la base de datos
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Masivocapital09*/",
    "database": "Dispositivos"
}

# Ruta para obtener dispositivos con sus ubicaciones y mediciones
@app.route('/api/dispositivos', methods=['GET']) #Define una URL (/api/dispositivos) donde se podrá hacer una solicitud GET para obtener los datos.
def get_dispositivos(): #Función que ejecutará la consulta a la base de datos
    try:
        connection = mysql.connector.connect(**db_config)#Se conecta a la base de datos MySQL usando la configuración definida.
        cursor = connection.cursor(dictionary=True) # Crea un cursor que devolverá los resultados como diccionarios ({columna: valor}).

        sql = """
            SELECT d.id_dispositivo, d.nombre, d.descripcion, 
                   u.latitud, u.longitud, 
                   GROUP_CONCAT(CONCAT(m.tipo_medicion, ': ', m.valor, ' ', m.unidad) SEPARATOR ', ') AS mediciones
            FROM Dispositivos d
            LEFT JOIN Ubicaciones u ON d.id_dispositivo = u.id_dispositivo
            LEFT JOIN Mediciones m ON d.id_dispositivo = m.id_dispositivo
            GROUP BY d.id_dispositivo, u.latitud, u.longitud;
        """ #Consulta 

        cursor.execute(sql) # Ejecuta la consulta en la base de datos.
        results = cursor.fetchall() # Recupera todos los resultados.

        cursor.close() #Cierra la conexion 
        connection.close()

        return jsonify(results) #Convierte los datos en JSON
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500 #Captura de error 

if __name__ == '__main__':
    print("Iniciando la aplicación Flask...")
    app.run(debug=True, port=3000, host="0.0.0.0")  #Inicia el servidor