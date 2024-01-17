from flask import Flask, jsonify
from mainSensores import last_ph_measurement

app = Flask(__name__)

@app.route('/ph')
def obtener_datos():
    datos = {
        'ph': last_ph_measurement if last_ph_measurement is not None else 7.0,  
        'humedad': 50,  
        'luz': 80,      
        'fertilizante': 30,  
        'agua': 60      
    }
    return jsonify(datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
