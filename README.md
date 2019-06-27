# garage_pi

This is a simple project which lets you open and close your garage door using a Sommer garage door opener, a Raspberry Pi Zero, MQTT and Home Assistant.
In order to controll the garage door opener from the company Summer, I bought the "Connex" addon PCB which extends the wall controller with two inputs. The "Connex" PCB is providing 24 VDC as an outlet for the inputs, therefore I connected the GPIO pins of the Pi to a relay which is then connected to the "Connex" PCB. 

# Requirements
## Hardware
* Raspberry Pi Zero W (or any other version)
* Power supply for Pi
* 2 Channel relais
* 4 cables (to connect relay with pi)
* 3 cables (to connect relay with Connex PCB)
* garage door opener pro+ (Sommer)
* Connex adaptor (Sommer)

## Software
* paho-mqtt
* RPi.GPIO

`sudo apt install -y pip python-rpi.gpio` `sudo pip install paho-mqtt`

# Installation

Inside the wall controller there is certian place for a battery pack. Due to the fact that I don't use the battery I used this space to place the Pi and the relay to. I cut a thin (3mm thick) wood plate so that it fit in that space and mounted the Pi and the relay onto the plate 
