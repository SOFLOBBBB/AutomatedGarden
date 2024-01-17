from machine import ADC, Pin
import time

ph_sensor_pin = 26
adc = ADC(Pin(ph_sensor_pin))

def read_ph_value():
    raw_value = adc.read_u16()
    ph_value = raw_value * 14.0 / 65535.0
    return ph_value

last_ph_measurement = None  # Variable para almacenar la última medición de pH

try:
    while True:
        ph_measurement = read_ph_value()
        last_ph_measurement = ph_measurement  # Almacena la última medición
        print("pH Value:", ph_measurement)
        time.sleep(1)

except KeyboardInterrupt:
    print("Medición de pH detenida por el usuario. ")
