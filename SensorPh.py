from machine import ADC, Pin
import time

# Configuración del pin ADC
ph_sensor_pin = 26  
adc = ADC(Pin(ph_sensor_pin))

def read_ph_value():
    # Lee el valor del sensor y convierte a pH  
    raw_value = adc.read_u16()
    ph_value = raw_value * 14.0 / 65535.0  # 0-14 rango pH 
    
    return ph_value

try:
    while True:
        ph_measurement = read_ph_value()
        print("pH Value:", ph_measurement)
        time.sleep(1)

except KeyboardInterrupt:
    print("Medición de pH detenida por el usuario. ")
