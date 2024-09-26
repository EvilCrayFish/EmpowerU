"""
#TODO File header pls
"""

# Third party imports
import tkinter as tk

# Local application imports
from interfaces.gui_main_window import EmpowerU

def main():
    """
    The main function definition.

    Parameters:
    (None)

    Returns:
    (None)
    """
    root = EmpowerU(title="Music School Management System", width=720, height=480)
    root.mainloop()
    print("MSMS proper shutdown completed.")


if __name__ == "__main__":
    # DO NOT MODIFY
    main()
