
import board
import digitalio



def init_snes(latch, clk, data):
    latch.direction = digitalio.Direction.OUTPUT
    clk.direction = digitalio.Direction.OUTPUT
    data.direction = digitalio.Direction.INPUT

'''
Reads the buttons from the SNES controller
'''
def get_snes_buttons(latch, clock, data, buttons):
    delaytime = 0.0001
    button_status = {'up' : 0, 'down' : 0, 'left' : 0, 'right' : 0, 'select' : 0, 'start' : 0, 'a' : 0, 'b' : 0}
    
    ## latch signal to retrieve pressed buttons
    latch.value = True
    sleep(delaytime)
    latch.value = False
    sleep(delaytime)

    ## get button data
    button_status[buttons[0]] = data.value 
    for x in range(0, 7, 1):
        clock.value = True
        sleep(delaytime)
        clock.value = False
        sleep(delaytime)
        button_status[buttons[x + 1]] = data.value
    return button_status