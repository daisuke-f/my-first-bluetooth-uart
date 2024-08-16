bluetooth.onBluetoothConnected(function () {
    connected = 1
    showConnected()
})
bluetooth.onBluetoothDisconnected(function () {
    connected = 0
    showDisconnected()
})
input.onButtonPressed(Button.A, function () {
    basic.showString("" + input.temperature() + "C")
})
function showDisconnected () {
    basic.showIcon(IconNames.Asleep)
    basic.pause(2000)
    basic.clearScreen()
}
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.Fullstop), function () {
    count += 1
    bluetooth.uartWriteLine("" + count + "," + input.temperature() + "," + pins.analogReadPin(AnalogPin.P0) + "," + pins.analogReadPin(AnalogPin.P3))
    basic.showIcon(IconNames.Happy)
    basic.pause(2000)
    basic.clearScreen()
})
function getBatteryMilliVolt () {
    mV = pins.analogReadPin(AnalogPin.P3) * (3000 / 1023)
}
input.onButtonPressed(Button.AB, function () {
    if (connected == 0) {
        showDisconnected()
    } else {
        showConnected()
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showString("" + (pins.analogReadPin(AnalogPin.P3)))
})
function showConnected () {
    basic.showIcon(IconNames.Happy)
    basic.pause(2000)
    basic.clearScreen()
}
let mV = 0
let count = 0
let connected = 0
bluetooth.startUartService()
connected = 0
count = 0
