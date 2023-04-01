"""Contains the GUI interface for using the methods in our Graph."""

import tkinter as tk
from typing import Callable

HEIGHT, WIDTH = 500, 500
FONT = ("HP Simplified Hans Light", 16)
LABEL_TEXT = "Select a method to use. Then, input the required arguments and press submit."


def build_button(frame: tk.Frame, text: str, function: Callable, row: int, col: int) -> None:
    """Given a frame, label text for a button, and a function to run, create a new button with those arguments
    and then place it on the frame at the specified row and column on a grid."""
    # Customization variables
    ipadx = 10
    ipady = 5
    bg = "#C3C2C2"
    pady = (50, 0)

    new_button = tk.Button(frame, text=text, padx=ipadx, pady=ipady, font=FONT, bg=bg, command=function)
    new_button.grid(row=row, column=col, pady=pady)


def build_graph() -> None:
    """The main method to generate the graph when ran."""
    root = tk.Tk()
    root.title("Language Graph GUI")
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.resizable(False, False)

    frame = tk.Frame(root)
    frame.pack()

    label = tk.Label(frame, text=LABEL_TEXT, font=FONT, wraplength=450)
    label.grid(row=0, column=0, columnspan=3, pady=(50, 0))

    build_button(frame, "Button 1", lambda: print("1"), 1, 0)
    build_button(frame, "Button 2", lambda: print("2"), 1, 1)
    build_button(frame, "Button 3", lambda: print("3"), 1, 2)
    build_button(frame, "Button 4", lambda: print("4"), 2, 0)
    build_button(frame, "Button 5", lambda: print("5"), 2, 2)

    root.mainloop()


if __name__ == '__main__':
    build_graph()
