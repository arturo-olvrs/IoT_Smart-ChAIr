import time
import paho.mqtt.client as mqtt

# Configuración
BROKER = "localhost"
PORT = 1883
TOPIC = "casa/sala/temperatura"

# Inicializar el cliente
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

# Conectar al broker
print(f"🔄 Conectando al broker {BROKER}...")
client.connect(BROKER, PORT, 60)

# Iniciar un bucle en segundo plano para manejar la red
client.loop_start()

contador = 1

try:
    while True:
        mensaje = f"Temperatura actual: 2{contador}°C"
        print(f"📤 Publicando: '{mensaje}' en el tópico '{TOPIC}'")
        
        # Publicar el mensaje
        client.publish(TOPIC, mensaje)
        
        contador += 1
        if contador > 9: contador = 1 # Reiniciar contador para el ejemplo
        
        time.sleep(2)  # Esperar 2 segundos antes de enviar el siguiente

except KeyboardInterrupt:
    print("\n👋 Deteniendo el publicador...")
    client.loop_stop()
    client.disconnect()