import time
import paho.mqtt.client as mqtt

# Configuración
BROKER = "localhost"
PORT = 1883     # Default MQTT port
TOPIC = "casa/sala/temperatura"

# Callback que se ejecuta cuando el cliente se conecta al broker
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Conectado exitosamente al Broker!")
        # Nos suscribimos al tópico
        client.subscribe(TOPIC)
        print(f"👂 Escuchando en el tópico: '{TOPIC}'...")
    else:
        print(f"❌ Error de conexión. Código: {rc}")

# Callback que se ejecuta cuando llega un mensaje
def on_message(client, userdata, msg):
    print(f"📥 Mensaje recibido en [{msg.topic}]: {msg.payload.decode('utf-8')}")

# Inicializar el cliente (usando la API v2 de Paho)
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

# Asignar las funciones de callback
client.on_connect = on_connect
client.on_message = on_message

# Conectar al broker local de Mosquitto
client.connect(host=BROKER, port=PORT, keepalive=60)

# Mantener el programa ejecutándose en un bucle infinito escuchando mensajes
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\n👋 Saliendo del suscriptor...")