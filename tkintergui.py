import tkinter as tk
import webbrowser
from typing import Callable
from csv_reader import read_csv
from generate_visuals import generate_graph, highlight_path

HEIGHT, WIDTH = 600, 700
FONT = ("Calibri", 16)
LABEL_TEXT = "Select a method to use. Then, input the required arguments and press submit."
LANGUAGE_GRAPH = read_csv('csv/relevant_genus_languages.csv', 'csv/creole_languages.csv')


def spanning_tree_button(frame: tk.Frame) -> None:
    previous_input = frame.grid_slaves(row=3)
    if previous_input:
        previous_input[0].grid_forget()

    input_frame = tk.Frame(frame)
    input_frame.grid(row=3, column=0, rowspan=3, columnspan=3, pady=50)

    genus_box = tk.Text(input_frame, height=1, width=20, font=FONT, undo=True, pady=1, padx=1)
    genus_box.insert(tk.END, "Input Genus")
    genus_box.grid(row=0, column=0)

    build_button(input_frame, "Submit", lambda: _spanning_tree_generate(genus_box.get("0.0", tk.END)[:-1]), 1, 0)


def _spanning_tree_generate(genus: str) -> None:

    spanning_tree = LANGUAGE_GRAPH.create_spanning_tree(genus)
    generate_graph(spanning_tree, "generated_graph")
    webbrowser.open("generated_graph.html")


def location_graph_button(frame: tk.Frame) -> None:
    previous_input = frame.grid_slaves(row=3)
    if previous_input:
        previous_input[0].grid_forget()

    input_frame = tk.Frame(frame)
    input_frame.grid(row=3, column=0, rowspan=3, columnspan=3, pady=50)

    location_box = tk.Text(input_frame, height=1, width=20, font=FONT, undo=True, pady=1, padx=1)
    location_box.insert(tk.END, "Input Location")
    location_box.grid(row=0, column=0)

    build_button(input_frame, "Submit", lambda: _location_graph_generate(location_box.get("0.0", tk.END)[:-1]), 1, 0)


def _location_graph_generate(location: str) -> None:
    location_tree = LANGUAGE_GRAPH.location_based_graph(location)
    generate_graph(location_tree, "generated_graph")
    webbrowser.open("generated_graph.html")


def creole_graph_button(frame: tk.Frame) -> None:
    previous_input = frame.grid_slaves(row=3)
    if previous_input:
        previous_input[0].grid_forget()

    input_frame = tk.Frame(frame)
    input_frame.grid(row=3, column=0, rowspan=3, columnspan=3, pady=50)

    creole_box = tk.Text(input_frame, height=1, width=20, font=FONT, undo=True, pady=1, padx=1)
    creole_box.insert(tk.END, "Input Creole")
    creole_box.grid(row=0, column=0)

    build_button(input_frame, "Submit", lambda: _creole_graph_generate(creole_box.get("0.0", tk.END)[:-1]), 1, 0)


def _creole_graph_generate(creole: str) -> None:
    creole_tree = LANGUAGE_GRAPH.creole_based_graph(creole)
    generate_graph(creole_tree, "generated_graph")
    webbrowser.open("generated_graph.html")


def highlight_path_button(frame: tk.Frame) -> None:
    previous_input = frame.grid_slaves(row=3)
    if previous_input:
        previous_input[0].grid_forget()

    input_frame = tk.Frame(frame)
    input_frame.grid(row=3, column=0, rowspan=3, columnspan=3, pady=50)

    start_box = tk.Text(input_frame, height=1, width=20, font=FONT, undo=True, pady=1, padx=1)
    start_box.insert(tk.END, "Input Start")
    start_box.grid(row=0, column=0)

    destination_box = tk.Text(input_frame, height=1, width=20, font=FONT, undo=True, pady=1, padx=1)
    destination_box.insert(tk.END, "Input Destination")
    destination_box.grid(row=1, column=0)

    build_button(input_frame, "Submit", lambda: _highlight_path(
        start_box.get("0.0", tk.END)[:-1],
        destination_box.get("0.0", tk.END)[:-1]
    ), 2, 0)


def _highlight_path(start: str, end: str) -> None:
    highlight_path(LANGUAGE_GRAPH, start, end, "generated_graph")
    webbrowser.open("generated_graph.html")


def entire_graph_button(frame: tk.Frame) -> None:
    input_frame = tk.Frame(frame)
    input_frame.grid(row=3, column=0, rowspan=3, columnspan=3, pady=50)

    languages_graph = read_csv('csv/relevant_genus_languages.csv', 'csv/creole_languages.csv')
    generate_graph(languages_graph, "generated_graph")

    webbrowser.open("generated_graph.html")


def build_button(frame: tk.Frame, text: str, function: Callable, row: int, col: int) -> None:
    ipadx = 10
    ipady = 5
    bg = "#C3C2C2"
    pady = (50, 0)

    new_button = tk.Button(frame, text=text, padx=ipadx, pady=ipady, font=FONT, bg=bg, command=function)
    new_button.grid(row=row, column=col, pady=pady)


def build_graph() -> None:
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
    build_button(frame, "Graph Creole", lambda: creole_graph_button(frame), 1, 2)
    build_button(frame, "Highlight Path", lambda: highlight_path_button(frame), 2, 0)
    build_button(frame, "Display Graph", lambda: entire_graph_button(frame), 2, 2)

    root.mainloop()


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['E9999']
    })

    build_graph()
