import json

import paho.mqtt.client as mqtt
from datetime import datetime

from database import db_save_message

# MQTT Broker Configuration
mqtt_broker_address = "broker.emqx.io"
mqtt_port = 1883
mqtt_keep_alive = 60
mqtt_topic = "testtopic/#"


# Connection success callback
def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))


# Callback function when a message is received
def on_message(client, userdata, message):
    payload = message.payload.decode()
    try:
        payload = json.loads(payload)
    except:
        pass
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Received message at {timestamp}: {payload}")

    # Save the message to the database MongoDB
    db_save_message(payload, timestamp)


def run_mqtt_subscriber():
    client = mqtt.Client()

    # Set the callback function
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to the MQTT broker
    client.connect(mqtt_broker_address, mqtt_port, mqtt_keep_alive)
    client.subscribe(mqtt_topic)
    client.loop_forever()


# Run the application
if __name__ == "__main__":
    run_mqtt_subscriber()
