import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import multiprocessing

import user_data as ud

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("home/SmartLigth/callback")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def mqttCreate():
    client = mqtt.Client()
    client.username_pw_set(ud.username, password=ud.password)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(ud.hostname, 1883, 60)

    client.loop_forever()

mt = multiprocessing.Process(target=mqttCreate)
mt.start()
