import logging

from ControlLib.ControlLib.src.my_cart import MyCart
import ControlLib.ControlLib.src.raw.can_messages as msg

class Keyboard_Tester:

    def __init__(self, cart: MyCart) -> None:
        # Components
        self.cart = cart

        # Setup the message logging
        self.logger = logging.getLogger("keyboard")
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(self.cart.config["logging_path"] + "keyboard.log")
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
        self.logger.addHandler(file_handler)

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
        while(True):
            self.perodic()

    # Periodic Loop
    def perodic(self):
        key = input()

        self.logger.info(key)
        self.button_map[key]()

    def noAction(self):
        pass
