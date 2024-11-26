from machine import I2C, Pin
from machine_i2c_lcd import I2cLcd
import time

# Initialize I2C interface
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Adjust pins as needed

# Define the I2C address of the LCD (from i2c.scan())
I2C_ADDR = 0x27

# Create LCD object for a 16x2 display
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

# Test: Display "Hello World" and update every second
while True:
    lcd.clear()                 # Clear the display
    lcd.putstr("Hey")  # Print "Hello World!" on the LCD
    time.sleep(5)               # Wait for 1 second
    lcd.clear()                 # Clear the display
    lcd.putstr("My name is")   # Print another test message
    lcd.move_to(0, 1)           # Move to the second line
    lcd.putstr("Peter")   # Print on the second line
    time.sleep(3)               # Wait for 1 second

