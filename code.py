import board
import digitalio
import analogio
import usb_hid

from hid_gamepad import Gamepad
import snes_gamepad as sg


# configure pins
latch = digitalio.DigitalInOut(board.GP20)  # output GPIO22
clk = digitalio.DigitalInOut(board.GP27)   # output GPIO21
data = digitalio.DigitalInOut(board.GP26)  # input GPIO5
buttons = {0: 'a', 1: 'b', 2: 'select', 3: 'start',
           4: 'up', 5: 'down', 6: 'left', 7: 'right'}

# initializations
gp = Gamepad(usb_hid.devices)
sg.init_snes(latch, clk, data)

while True:
    # Buttons are grounded when pressed (.value = False).
    button_status = sg.get_snes_buttons(latch, clk, data, buttons)
    for x in buttons:
        if button_status[buttons[x]] == True:
            gp.release_buttons(x + 1)
        else:
            gp.press_buttons(x + 1)

