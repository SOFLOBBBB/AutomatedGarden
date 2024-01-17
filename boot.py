import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('INFINITUM6702', 'QpnKM3PayX')

while not wlan.isconnected():
    pass

print('Conexión exitosa. IP:', wlan.ifconfig()[0])
