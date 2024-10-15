import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define the GPIO pin
LED_PIN = 18

# Set up the LED pin as an output
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    # Turn on the LED
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("LED is ON")
    time.sleep(2)  # LED stays on for 2 seconds

    # Turn off the LED
    GPIO.output(LED_PIN, GPIO.LOW)
    print("LED is OFF")

finally:
    # Clean up the GPIO settings
    GPIO.cleanup()
