"""
A simple script to turn on/off a WS2812 LED strip based on the state of a pair of slotted opto-couplers
mounted on the 2 doors of a cabinet.

Here is the specific model of optocoupler:
    https://www.amazon.com/dp/B08977QFK5?psc=1&ref=ppx_yo2ov_dt_b_product_details

Truth table:
    |-----------------|---------------------------------|
    |    Doors        |    Opto-Couplers                |
    |-----------------|---------------------------------|-----------|
    | Left   | Right  | Left           | Right          | LED Strip |
    |--------|--------|----------------|----------------|-----------|
    | Closed | Closed | Blocked        | Blocked        | Off       |
    | Open   | Closed | Unblocked      | Blocked        | On        |
    | Closed | Open   | Blocked        | Unblocked      | On        |
    | Open   | Open   | Unblocked      | Unblocked      | On        |
    |--------|--------|----------------|----------------|-----------|

    "Blocked" = no light detected on the coupler receiver
    "Unblocked" = light detected on the coupler receiver

Tested on:
   MicroPython v1.21.0 on 2023-10-06; Raspberry Pi Pico with RP2040

"""
import neopixel
from machine import Pin
import time

# Pin configuration
left_door_optocoupler_pin = Pin(0, Pin.IN, Pin.PULL_UP)
right_door_optocoupler_pin = Pin(1, Pin.IN, Pin.PULL_UP)
led_strip_pin = Pin(22)

# Number of WS2812 LEDs in the strip
num_leds = 55

# Initialize the WS2812 LED strip
led_strip = neopixel.NeoPixel(led_strip_pin, num_leds)

# LED strip color values
OFF = (0, 0, 0)  # Nothing
ON = (255, 255, 255)  # White


def control_led_strip(optocoupler_state):
    """
    Control the LED strip based on optocoupler state

    :param optocoupler_state: Either True (door open) or False (door closed)
    :type optocoupler_state: bool
    :return: Nothing
    :rtype: None
    """
    if optocoupler_state:
        # Door open - Unblocked, light detected
        led_strip.fill(ON)
    else:
        # Door closed - Blocked, no light detected
        led_strip.fill(OFF)

    # Update the LED strip
    led_strip.write()


# Main loop
while True:
    # Read the state of the optocouplers
    state = bool(left_door_optocoupler_pin.value()) or bool(right_door_optocoupler_pin.value())

    # Control the LED strip based on the optocoupler state
    control_led_strip(state)

    time.sleep(0.1)
