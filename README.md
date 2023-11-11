# ME35-Temperature
Jordan Berke's ME 35 Temperature regulation system code

Basic Information:

Micropython libraries used: PIN, PWM, ADC, network, time, machine

Personally constructed libraries used: simple.py - library created for the connection of microcontroller to an MQTT client
                                       controller.py - library created for the configuration and use of an Adafruit I2C gamepad controller

This repository contains files used in the construction of a temperature regulation that system that can
- reads the temperature of an environment
- give a visual aid to the user of the rough temperature of the environment
- allow the user to "turn on" a temperature regulation device
- change the temperature units based on the color of an object held in front of the computer camera

NOTE: some code has been removed involving personal information for publishing to an Adafruit dashboard. Additional information on how to create your own dashboard can be found on the adafruit.io webpage

