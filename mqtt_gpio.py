#!/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

# MQTT setup
MQTT_BROKER = "192.168.xxx.xxx"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = [("garage/auf",1),("garage/zu",1)]

# GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT) # Channel 1 auf dem Relais
GPIO.output(15, GPIO.LOW)
GPIO.setup(16, GPIO.OUT) # Channel 2 auf dem Relais
GPIO.output(16, GPIO.LOW)

try:
    def on_connect(client, userdata, flags, rc):
        if rc==0:
            print "Connection to " + MQTT_BROKER + " ok, returned code: " + str(rc)
        else:
            print "Not connected, returned code" ,rc

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(MQTT_TOPIC, 0)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        if (msg.topic=='garage/auf') and (msg.payload=='ON'):
            GPIO.output(15,True)
            print "Topic:" +str(msg.topic)
            print "Payload:" +str(msg.payload)
        elif (msg.topic=='garage/auf') and (msg.payload=='OFF'):
            GPIO.output(15,False)
            print "Topic:" +str(msg.topic)
            print "Payload:" +str(msg.payload)
        if (msg.topic=='garage/zu') and (msg.payload=='ON'):
            GPIO.output(16,True)
            print "Topic:" +str(msg.topic)
            print "Payload:" +str(msg.payload)
        elif (msg.topic=='garage/zu') and (msg.payload=='OFF'):
            GPIO.output(16,False)
            print "Topic:" +str(msg.topic)
            print "Payload:" +str(msg.payload)

    def on_subscribe(mosq, obj, mid, granted_qos):
        print("Subsribed to Topic:" + MQTT_TOPIC)
    

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe

    client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()

except KeyboardInterrupt:
    GPIO.cleanup()
