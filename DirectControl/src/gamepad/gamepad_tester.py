from DirectControl.src.ControlLib.ControlLib.src.my_cart import MyCart
from DirectControl.src.gamepad.controller import Gamepad

class Gamepad_Tester:

    def __init__(self, cart: MyCart, gamepad: Gamepad) -> None:
        # Components
        self.cart = cart
        self.gamepad = gamepad

        # Controller Buttons
        self.button_map = {
            'BTN_TL': self.noAction,
            'BTN_TR': self.noAction,
            'BTN_NORTH': self.cart.forwards,
            'BTN_EAST': self.cart.enableAccelerator,
            'BTN_SOUTH': self.cart.reverse,
            'BTN_WEST': self.cart.disableAccelerator,
            'BTN_THUMBL': self.cart.leftSignal,
            'BTN_THUMBR': self.cart.rightSignal,
            'BTN_START': self.shutdown,
            'BTN_SELECT': self.noAction,
            'DPAD_NORTH': self.cart.brake,
            'DPAD_SOUTH': self.cart.disengageBrakes,
            'DPAD_EAST': self.noAction,
            'DPAD_WEST': self.noAction

        }

        self.stick_map = {
            'LSTICK_X': self.turn,
            'LSTICK_Y': self.noAction,
            'RSTICK_X': self.noAction,
            'RSTICK_Y': self.my_cart.setSpeed

        }

        self.trigger_map = {
            'ABS_Z': self.noAction,
            'ABS_RZ': self.noAction

        }

    def run(self):
        self.gamepad.startListener()

        while(True):
            self.perodic()

    # Periodic Loop
    def perodic(self):
        for button_event in self.gamepad.buttons.keys():
            if self.gamepad.buttons[button_event]:
                self.button_map[button_event]()

        for stick_event in self.gamepad.sticks.keys():
            self.stick_map[stick_event](self.gamepad.sticks[stick_event])

        for trigger_event in self.gamepad.triggers.keys():
            self.trigger_map[trigger_event](self.gamepad.triggers[trigger_event])
            
                    

    def noAction(self):
        pass

    def turn(self, power = 0):
        if power > 0:
            self.cart.turnLeft(power)
        elif power < 0:
            self.cart.turnRight(power)
        else:
            self.cart.stopTurn()