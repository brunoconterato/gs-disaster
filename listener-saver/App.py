import paho.mqtt.client as mqtt
import json
import time
import SensorData
from db.database_session import get_db

# MQTT Credentials
MQTT_BROKER = "759d2f782c6f48d68eafab33492641f8.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_USER = "sla"
MQTT_PASSWORD = "sla"

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
        
        # Map ESP32 data to database schema
        sensor_entry = SensorData(
            station_id=data.get("station_id", "unknown"),
            measure_time=data.get("timestamp", ""),
            river_level_cm=data.get("river_level_cm", 0.0),
            temperature_c=data.get("temperature", 0.0),
            air_humidity_pct=data.get("soil_moisture_pct", 0.0),
            rain_analog=data.get("rain_mm", 0.0)
        )
        
        # Save to database
        with get_db() as db:
            db.add(sensor_entry)
            db.commit()
        print(f"Saved to DB: {sensor_entry.station_id} at {sensor_entry.measure_time}")
        
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