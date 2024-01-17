# Este script intentará obtener la dirección IP de la interfaz WLAN
# (Wireless LAN) de la Raspberry Pi Pico W.
import network

def obtener_direccion_ip(interface='wlan0'):
    wlan = network.WLAN(network.STA_IF)
    direccion_ip = None

    if wlan.active():
        direccion_ip = wlan.ifconfig()[0]

    return direccion_ip

direccion_ip_raspberry_pico_w = obtener_direccion_ip()
print("Dirección IP de la Raspberry Pi Pico W:", direccion_ip_raspberry_pico_w)

# wlan0 eth0 usb0