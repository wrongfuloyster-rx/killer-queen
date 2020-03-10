import paho.mqtt.client as mqtt
import json
import pprint
import time
from datetime import datetime
from twisted.internet import task
from twisted.internet.task import LoopingCall
from twisted.internet import reactor

#configure MQTT client
client = "osnds-dev-client-publish"
server = "mqtt.eclipse.org"
port = 1883
keepalive = 45

#establish connection to MQTT server
mqttc = mqtt.Client(client)
mqttc.connect(server,port,keepalive)

#function to publish message to MQTT broker
def publishMessage():
    msg = {
        "message number:":"Hi",
        "time elapsed":time.time(),
    }
    msg = json.dumps(msg)
    pprint.pprint(msg)
    mqttc.publish("osnds-dev-test/sensor_test", msg)

LoopingCall(publishMessage).start(0.0001)
reactor.run()
