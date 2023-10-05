import paho.mqtt.client as mqtt
from datetime import datetime

# MQTT Broker Configuration
mqtt_broker_address = "broker.emqx.io"
mqtt_port = 1883
mqtt_keep_alive = 60
mqtt_topic = "testtopic/#"

# Initialize the MQTT client
client = mqtt.Client()


# Connection success callback
def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))


# Callback function when a message is received
def on_message(client, userdata, message):
    payload = message.payload.decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Received message at {timestamp}: {payload}")

    # Save the message to the database MongoDB


# Set the callback function
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(mqtt_broker_address, mqtt_port, mqtt_keep_alive)
client.subscribe(mqtt_topic)
client.loop_start()

# Run the application
try:
    while True:
        pass
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
