# Third party imports
import tkinter as tk

# Local application imports
from testing_gui import Page

def main():
    """
    The main function definition.

    Parameters:
    (None)

    Returns:
    (None)
    """
    root = Page(title="Music School Management System", width=720, height=480)
    root.mainloop()
    print("MSMS proper shutdown completed.")


if __name__ == "__main__":
    # DO NOT MODIFY
    main()
