import paho.mqtt.client as mqttClient
import time
import RPi.GPIO as GPIO

# Variables
broker_address= "192.168.x.x"                        #Broker address
port = 1883                                          #Broker port
user = "user"                                        #Connection username
password = "password"                                #Connection password

# GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)                             # Channel 1 auf dem Relais
GPIO.output(15, GPIO.LOW)
GPIO.setup(16, GPIO.OUT)                             # Channel 2 auf dem Relais
GPIO.output(16, GPIO.LOW)


def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
        print("Connection to " + broker_address + " ok, returned code: " + str(rc))
 
        global Connected                            #Use global variable
        Connected = True                            #Signal connection 
 
    else:
        print("Connection failed")
 
def on_message(client, userdata, message):
    message.payload = message.payload.decode("utf-8")
    Command = message.payload
    print("Message received: " + Command)
    if Command == "open":
        GPIO.output(15,True)
        time.sleep(0.1)
        GPIO.output(15,False)
        time.sleep(5)
        print("Changing state to: opened")
        client.publish("garage/state", "opened")
    elif Command == "close":
        GPIO.output(16,True)
        time.sleep(0.1)
        GPIO.output(16,False) 
        time.sleep(5)
        print("Changing state to: closed")
        client.publish("garage/state", "closed")
 
Connected = False                                  #global variable for the state of the connection
 
client = mqttClient.Client("Garage")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
 
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()                                #start the loop
 
while Connected != True:                           #Wait for connection
    time.sleep(0.1)
 
client.subscribe("garage/#")
 
try:
    while True:
        time.sleep(0.1)
            
except KeyboardInterrupt:
    print("exiting")
    GPIO.cleanup() 
    client.disconnect()
    client.loop_stop()
