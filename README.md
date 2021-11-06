# SNEStoPC
Raspberry pico SNES->USB adapter

Uses CircuitPython as base. 
## Installation
- plug in the raspberry pico while holding BOOTSEL and install CircuitPython 7.x.x. Once done, unplug the USB cable.
- using a logic level adapter connect data line to GP26, clock to GP27 and latch to GP20. More info: https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide/all
- Plug the USB and drag the code into the Circuitpython external drive.

# Based on:
- https://github.com/printnplay/Pico-MicroPython/blob/main/NES2USB.py
- https://github.com/adafruit/Adafruit_CircuitPython_HID
