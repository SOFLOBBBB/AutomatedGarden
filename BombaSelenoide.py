import machine
import utime

# pin GPIO al que está conectado el pin de control del relé
pin_rele = machine.Pin(15, machine.Pin.OUT)  

def activar_bomba(potencia):
    pin_rele.value(1)  # Activa el relé (y por ende la bomba solenoide)
    utime.sleep(potencia / 100.0)  # Duración proporcional a la potencia

def desactivar_bomba():
    pin_rele.value(0)  # Desactiva el relé (y por ende la bomba solenoide)

def main():
    try:
        while True:
            print(f"Activando la bomba al {potencia_optima}%...")
            activar_bomba(potencia_optima)
            utime.sleep(5)  # Mantiene la bomba activada durante 5 segundos

            print(f"Activando la bomba al {potencia_maxima}%...")
            activar_bomba(potencia_maxima)
            utime.sleep(5) 

            print("Desactivando la bomba...")
            desactivar_bomba()
            utime.sleep(10)  # Se espera 10 segundos antes de activar la bomba nuevamente

    except KeyboardInterrupt:
        print("Programa interrumpido manualmente")

if __name__ == "__main__":
    # Configuración de la potencia
    potencia_optima = 75  # Porcentaje de potencia óptima
    potencia_maxima = 100  # Porcentaje de potencia máxima
    
    main()