"""
#TODO File header pls hiiiiiiiii
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
    root = EmpowerU(title="EmpowerU", width=1280, height=720)
    root.mainloop()
    print("EmpowerU proper shutdown completed.")


if __name__ == "__main__":
    # DO NOT MODIFY
    main()
