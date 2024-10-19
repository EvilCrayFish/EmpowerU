"""
FIT1056 2024 Semester 2
EmpowerU Project
Team G08

This file should be the one that is run to start the application.
"""

# Imports
import tkinter as tk
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
