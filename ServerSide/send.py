import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

import user_data as ud

client = mqtt.Client()
client.connect(ud.hostname, 1883, 60)
while True:
    cmd = input()
    publish.single("home/SmartLigth/request", cmd + "\n", hostname=ud.hostname, qos=2, auth= ud.auth )
