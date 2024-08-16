def on_bluetooth_connected():
    global connected
    connected = 1
    showConnected()
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global connected
    connected = 0
    showDisconnected()
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_button_pressed_a():
    basic.show_string("" + str(input.temperature()) + "C")
input.on_button_pressed(Button.A, on_button_pressed_a)

def showDisconnected():
    basic.show_icon(IconNames.ASLEEP)
    basic.pause(2000)
    basic.clear_screen()

def on_uart_data_received():
    bluetooth.uart_write_line("" + str(input.temperature()) + "," + str(pins.analog_read_pin(AnalogPin.P0)) + "," + str(pins.analog_read_pin(AnalogPin.P3)))
    basic.show_icon(IconNames.HAPPY)
    basic.pause(2000)
    basic.clear_screen()
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.FULLSTOP),
    on_uart_data_received)

def getBatteryMilliVolt():
    global mV
    mV = pins.analog_read_pin(AnalogPin.P3) * (3000 / 1023)

def on_button_pressed_ab():
    if connected == 0:
        showDisconnected()
    else:
        showConnected()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("" + str((pins.analog_read_pin(AnalogPin.P3))))
input.on_button_pressed(Button.B, on_button_pressed_b)

def showConnected():
    basic.show_icon(IconNames.HAPPY)
    basic.pause(2000)
    basic.clear_screen()
mV = 0
connected = 0
bluetooth.start_uart_service()
connected = 0