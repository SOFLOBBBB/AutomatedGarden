from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/datos_sensor')
def obtener_datos_sensor():
    # Lógica para obtener los datos del sensor aquí
    datos_sensor = {'ph': 7.0, 'humedad': 50, 'luz': 80, 'fertilizante': 30, 'agua': 60}
    return jsonify(datos_sensor)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
