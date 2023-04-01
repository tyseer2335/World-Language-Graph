"""Contains the GUI interface for using the methods in our Graph."""

import tkinter as tk
from typing import Callable

HEIGHT, WIDTH = 600, 700
FONT = ("Calibri", 16)
LABEL_TEXT = "Select a method to use. Then, input the required arguments and press submit."


def spanning_tree_button(frame: tk.Frame) -> None:
    """Generates the required input fields to call the spanning tree method on the inputted frame."""
    input_frame = tk.Frame(frame)
    input_frame.grid(row=3, column=0, rowspan=3, columnspan=3, pady=50)

    genus_box = tk.Text(input_frame, height=1, width=20, font=FONT, undo=True, pady=1, padx=1)
    genus_box.insert(tk.END, "Input Genus")
    genus_box.grid(row=0, column=0)

    build_button(input_frame, "Submit", lambda: print(genus_box.get("0.0", tk.END)[:-1]), 1, 0)


def location_graph_button(frame: tk.Frame) -> None:
    """Generates the required input fields to call the spanning tree method on the inputted frame."""
    input_frame = tk.Frame(frame)
    input_frame.grid(row=3, column=0, rowspan=3, columnspan=3, pady=50)

    location_box = tk.Text(input_frame, height=1, width=20, font=FONT, undo=True, pady=1, padx=1)
    location_box.insert(tk.END, "Input Location")
    location_box.grid(row=0, column=0)

    build_button(input_frame, "Submit", lambda: print(location_box.get("0.0", tk.END)[:-1]), 1, 0)


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

    label = tk.Label(frame, text=LABEL_TEXT, font=FONT, wraplength=650)
    label.grid(row=0, column=0, columnspan=3, pady=(50, 0))

    build_button(frame, "Spanning Tree", lambda: spanning_tree_button(frame), 1, 0)
    build_button(frame, "Graph Location", lambda: location_graph_button(frame), 1, 1)
    build_button(frame, "Graph Creole", lambda: print("3"), 1, 2)
    build_button(frame, "Shortest Distance", lambda: print("4"), 2, 0)
    build_button(frame, "Button 5", lambda: print("5"), 2, 2)

    root.mainloop()


if __name__ == '__main__':
    build_graph()
