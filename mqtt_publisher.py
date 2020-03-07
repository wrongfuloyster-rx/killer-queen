import paho.mqtt.client as mqtt
import json
import pprint
import time
import math
import geohash2

from random import random
from random import seed

i=1
seed(1)
count = 0
geo = geohash2.encode(28.415548, -80.611178)

def on_publish(client, userdata, mid):
    print("Message Published to MQTT ...")

mqttc = mqtt.Client("osnds-dev-client")
mqttc.on_publish = on_publish
mqttc.connect("mqtt.eclipse.org",port=1883,keepalive=45)

#add sleep(1/samples-per-second) to publisher loop

try:
    while True:
        rand = random()
        it = i
        message = {
            "count":i,
            "random": rand,
        }
        msg = json.dumps(message)
        pprint.pprint(msg)
        mqttc.publish("osnds-dev-test/sensor_test", msg)
        i = i+1
except KeyboardInterrupt:
    pass

mqttc.disconnect()
time.sleep(2)
