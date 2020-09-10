#FLIGHT CONTROLER 101
#Written by Felix Gateru Wanyoike and Washington Kigani Kamadi


#Importing modules to be used, i2c, PWM, UART and time
from machine import Pin, PWM, I2C, UART
import machine, ubinascii, time, math

uart = UART(1, 9600)
uart.init(9600, bits=8, parity=None, stop=1)

#GPIO pins assigned as PWM for each of the motors
#The pins will control the motor speeds for each motor of the quad
esc0 = PWM(Pin(0))
esc1 = PWM(Pin(1))
esc2 = PWM(Pin(2))
esc3 = PWM(Pin(3))

#Setting the frequency to 2MHz
#Frequency for each of the motors
esc0.freq(2000)
esc1.freq(2000)
esc2.freq(2000)
esc3.freq(2000)

#Setting up I2C to read from IMU at address 0x62
#We will use the hardware i2c
imu = I2C(0)
imu = I2C(1, scl=Pin(5), sda=Pin(4), freq=400000)

#Scanning from slave devices
imu.scan()


while True:
    #Flight control logic here


#Functions to process the values read from the imu via i2c
#The values read are converted to angles that will be used for flight control
def anglex( ):
    #Reading the required number of bytes from the address of x angle
    #The address and number of bytes to be adjusted depending on imu used
    Xangle = imu.readfrom(0x68, 8) 
    #Process value to give angle
    return Xangle

def angley( ):
    
    return Yangle

def anglez( ):
    
    return Zangle