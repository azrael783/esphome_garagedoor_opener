# esphome_garagedoor_opener

This is a simple project which lets you open and close your garage door using a [Sommer](https://www.sommer.eu/en-GB/) garage door opener, an ESP8266 flashed with [ESPHOME](https://www.esphome.io) and Home Assistant.
In order to controll the garage door opener from the company Summer, I bought the "Connex" addon PCB which extends the wall controller with two inputs. The "Connex" PCB is providing 24 VDC as an outlet for the inputs, therefore I connected the GPIO pins of the ESP8266 to a relay which is then connected to the "Connex" PCB. 

# Requirements
## Hardware
* NodemcuV3 (or any other ESP device which is supported by esphome)
* 5V Power supply
* 2 Channel relais
* 4 cables (to connect relay with pi)
* 3 cables (to connect relay with Connex PCB)
* garage door opener [pro+](https://www.sommer.eu/en-GB/pro-base.html) (Sommer) 
* [Connex](https://www.sommer-shops.eu/de/conex.html) adaptor (Sommer)

## Software
* firmware created with ESPHOME

# Installation
## Hardware

Inside the wall controller there is certian place for a battery pack. Due to the fact that I don't use the battery I used this space to place the Pi and the relay to. I cut a thin (3mm thick) wood plate so that it fit in that space and mounted the Pi and the relay onto the plate. The plate is then fixed with double sided tape into the housing. Before I fixed the plate in the housing I did the wiring from the Pi to the relay and from the relay to the Connex PCB. I used pins 15 and 16 to connect to the relay. If you use other pins, please adapt the mqtt_gpio.py script.


## Software
work in progress
