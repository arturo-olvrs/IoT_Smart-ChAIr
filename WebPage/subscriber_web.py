import paho.mqtt.client as mqtt
from flask import Flask, render_template
from flask_socketio import SocketIO

# Configuración de Flask y SocketIO
app = Flask(__name__)
# El secret_key es necesario para SocketIO (puedes poner lo que quieras)
app.config['SECRET_KEY'] = 'mi_secreto_super_seguro_123'
socketio = SocketIO(app, cors_allowed_origins="*")

# Configuración MQTT
BROKER = "localhost"
PORT = 1883
TOPIC = "casa/sala/temperatura"

# --- SECCIÓN MQTT ---

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Conectado al Broker MQTT desde la Web!")
        client.subscribe(TOPIC)
    else:
        print(f"❌ Error de conexión MQTT. Código: {rc}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8')
    print(f"📥 MQTT -> Servidor Web: {payload}")
    
    # Aquí ocurre la magia: cuando llega un mensaje de MQTT,
    # se lo enviamos "en el acto" a la página web abierta usando WebSockets.
    socketio.emit('nuevo_mensaje', {'data': payload})

# Inicializar cliente MQTT
mqtt_client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(BROKER, PORT, 60)

# Iniciamos el bucle de MQTT en un hilo secundario para que no bloquee a Flask
mqtt_client.loop_start()


# --- SECCIÓN FLASK (WEB) ---

# Ruta principal de la web (al entrar a http://localhost:5000)
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # Arrancamos el servidor web en el puerto 5000
    print("🚀 Servidor Web iniciándose en http://localhost:5000")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)