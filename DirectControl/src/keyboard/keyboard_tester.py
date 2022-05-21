import logging
import keyboard
import time

from ControlLib.ControlLib.src.my_cart import MyCart
import ControlLib.ControlLib.src.raw.can_messages as msg

class Keyboard_Tester:

    def __init__(self, cart: MyCart) -> None:
        # Components
        self.cart = cart

        # Setup the message logging
        self.logger = logging.getLogger("keyboard")
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(self.cart.config["logging_path"] + "/keyboard.log")
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
        self.logger.addHandler(file_handler)

        # Previous Key Storage
        self.prev_key = 'b'

        # Controller Buttons
        self.button_map = {
            'w': self.cart.incAccel,
            's': self.cart.decAccel,
            'f': self.cart.forwards,
            'r': self.cart.reverse,
            'e': self.cart.enableAccelerator,
            'd': self.cart.disableAccelerator,
            'space': self.cart.brake,
            'b': self.cart.brake,
            'n': self.cart.disengageBrakes,
            'h': self.cart.honk,
            'i': self.cart.turnRight,
            'o': self.cart.turnLeft,
            'k': self.cart.stopTurn,
            '1': self.cart.leftSignal,
            '2': self.cart.rightSignal

        }

    def run(self):
        print("""
        w - Speed Up
        s - Slow Down
        f - Forwards
        r - Reverse
        e - Enable
        d - Disable
        space / b - Brake
        n - Release Brakes
        h - Honk Horn
        i - Turn Right
        o - Turn Left
        k - Stop Turning
        1 - Left Signal
        2 - Right Signal
        """)

        time.sleep(2)
        print("Enter Keystrokes")

        while(True):
            self.perodic()

    # Periodic Loop
    def perodic(self):
        # Get Key
        key = keyboard.read_key()
        self.logger.info(key)

        # Stop Turn if Not Pressed
        if self.prev_key in {'i','o'}:
            if key not in {'i','o'}:
                self.cart.stopTurn()

        # Key dictionary
        try:
            self.button_map[key]()
        except KeyError:
            pass

        # Update Prev Key
        self.prev_key = key

        # Sleep
        time.sleep(.1)
        

    def noAction(self):
        pass
