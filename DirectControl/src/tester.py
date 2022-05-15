import src.util as util

from ControlLib.ControlLib.src.my_cart import MyCart

from src.gamepad.gamepad_tester import Gamepad_Tester
from src.keyboard.keyboard_tester import Keyboard_Tester

# Hardware Module Tester
# Main
#
# Part of the GSSM Autonomous Golf Cart
# Written by: Joseph Telaak, class of 2022


class Tester:

    # Constructor
    def __init__(self, cart: MyCart) -> None:
        self.cart = cart

    # Run
    def run(self):
        try:
            self.main_menu()
        
        except KeyboardInterrupt:
            print("Exiting")
            pass

    # Main menu
    def main_menu(self):
        util.clear()
        print("Pick Control Method: ")

        print("""
            1) Keyboard
            2) Controller
            3) Exit
        
        """)

        try:
            option = int(input("Enter Choice: "))
        except:
            self.main_menu()

        if option == 1:
            tester = Keyboard_Tester(self.cart)
            tester.run()

        elif option == 2:
            tester = Gamepad_Tester(self.cart)
            tester.run()

        elif option == 3:
            exit(0)
        
        self.main_menu()

    