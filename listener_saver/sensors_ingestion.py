import paho.mqtt.client as mqtt
import json
import time
from db.database_session import get_db
from db.crud import create_sensor_measurement  

# MQTT Credentials
MQTT_BROKER = "759d2f782c6f48d68eafab33492641f8.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_USER = "sla"
MQTT_PASSWORD = "sla"

# Sensor mapeamento
SENSOR_MAPPING = {
    "river_level_cm": 1,
    "temperature": 2,
    "soil_moisture_pct": 3,
    "rain_mm": 4
}

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to MQTT broker (rc={rc})")
        client.subscribe("esp32/s0")
    else:
        print(f"Connection failed (rc={rc})")

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        print(f"Received from {msg.topic}: {payload}")
        
        data = json.loads(payload)
        
        timestamp = data.get("timestamp")
        data_source = "mqtt" 

        with get_db() as db:
            for field, sensor_id in SENSOR_MAPPING.items():
                measurement_value = data.get(field)
                if measurement_value is not None:
                    create_sensor_measurement(
                        db=db,
                        id_sensor=sensor_id,
                        measurement_value=measurement_value,
                        timestamp=timestamp,
                        data_source=data_source
                    )
                    print(f"Saved sensor {sensor_id}: {measurement_value} at {timestamp}")

    except Exception as e:
        print(f"Error processing message: {str(e)}")

# MQTT Client Setup
client = mqtt.Client()
client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
client.tls_set()  # Enable TLS
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)

print("Starting MQTT listener...")
client.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping...")
    client.loop_stop()
    client.disconnect()
