import sys

# Hardware Module Tester
# Main
#
# Part of the GSSM Autonomous Golf Cart
# Written by: Joseph Telaak, class of 2022

if __name__ == "__main__":
    # Version Check
    python_major = sys.version_info[0]
    python_minor = sys.version_info[1]
    python_version = str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])

    # Check for Python 3
    if python_major != 3 and python_minor != 7:
        print(f"The GSSM Auto Golf Cart CAN Tester Requires Python 3.7. You are using {python_version}")
        sys.exit(1)

    # Imports
    import src.util as util

    # Banner and Info Block
    print(util.to_color(util.title, "cyan"))
    print(util.info_block)

    # Check args
    if len(sys.argv) == 1:
        print(util.to_color("Please Specify the Serial Port of the CAN Adapter", "red"))
        print()

        sys.exit(1)

    # Imports
    from src.tester import Tester
    from src.ControlLib.ControlLib.src.my_cart import MyCart

    # Run Program
    tester = Tester(cart=MyCart("config.json"))
    tester.run()