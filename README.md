# garage_pi

This is a simple project which lets you open and close your garage door using a [Sommer](https://www.sommer.eu/en-GB/) garage door opener, a Raspberry Pi Zero, MQTT and Home Assistant.
In order to controll the garage door opener from the company Summer, I bought the "Connex" addon PCB which extends the wall controller with two inputs. The "Connex" PCB is providing 24 VDC as an outlet for the inputs, therefore I connected the GPIO pins of the Pi to a relay which is then connected to the "Connex" PCB. 

# Requirements
## Hardware
* Raspberry Pi Zero W (or any other version)
* Power supply for Pi
* 2 Channel relais
* 4 cables (to connect relay with pi)
* 3 cables (to connect relay with Connex PCB)
* garage door opener [pro+](https://www.sommer.eu/en-GB/pro-base.html) (Sommer) 
* [Connex](https://www.sommer-shops.eu/de/conex.html) adaptor (Sommer)

## Software
* paho-mqtt
* RPi.GPIO
* samba

`sudo apt install -y pip samba` `sudo pip install paho-mqtt RPi.GPIO`

# Installation
## Hardware

Inside the wall controller there is certian place for a battery pack. Due to the fact that I don't use the battery I used this space to place the Pi and the relay to. I cut a thin (3mm thick) wood plate so that it fit in that space and mounted the Pi and the relay onto the plate. The plate is then fixed with double sided tape into the housing. Before I fixed the plate in the housing I did the wiring from the Pi to the relay and from the relay to the Connex PCB. I used pins 15 and 16 to connect to the relay. If you use other pins, please adapt the mqtt_gpio.py script.
![breadboard scheme](https://github.com/azrarel783/garage_pi/blob/master/garage_pi.jpg)

## Software
Download the mqtt_gpio.py and the garage_opener.service files. Store the Python script in any folder on the Pi you like (I put mine in `/home/pi/garage_prog`), for easier maintenance I also installed samba und gave access to the "garage_prog" folder. You will find the configuration file for samba also in this repo. Adjust the mqtt-gpio.py to your MQTT broker by changing the variable "MQTT_BROKER". Please note that my broker doesn't need an user and password to connect.

Store the garage_opener.service file in `/etc/systemd/system/`, change the path in the .service accordingly to your path. Reload the daemon with `sudo systemctl daemon-reload` then enable the Python script to be auto started after Pi has started with `sudo systemctl enable garage_opener`. You can check the status with `sudo systemctl status garage_opener`. The Pyhton script will listen on two MQTT topics `garage/auf` and `garage/zu` which stands for door open and close. Create two MQTT switches in Home Assistant which will publish `on` if you activate them:
```
# configuration.yaml
switch:
  - platform: mqtt
    name: Garage auf
    icon: mdi:garage-open
    command_topic: "garage/auf"
    payload_on: "ON"
    payload_off: "OFF"
  - platform: mqtt
    name: Garage zu 
    icon: mdi:garage
    command_topic: "garage/zu"
    payload_on: "ON"
    payload_off: "OFF"
```
I then created two automations which immediately "turn off" the topic again: 
```
# automation.yaml
- id: garage_auf_auto_aus
  alias: Garage "auf" auto_aus
  trigger:
  - entity_id: switch.garage_auf
    for: 00:00:01
    from: 'off'
    platform: state
    to: 'on'
  condition: []
  action:
  - data:
      entity_id: switch.garage_auf
    service: homeassistant.turn_off
- id: garage_zu_auto_aus
  alias: Garage "zu" auto_aus
  trigger:
  - entity_id: switch.garage_zu
    for: 00:00:01
    from: 'off'
    platform: state
    to: 'on'
  condition: []
  action:
  - data:
      entity_id: switch.garage_zu
    service: homeassistant.turn_off
```
