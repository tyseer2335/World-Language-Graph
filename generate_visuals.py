"""This Python file genrates the visulizations from the Graph"""
from main import LanguageGraph
from pyvis.network import Network
from csv_reader import read_csv


def generate_graph(graph: LanguageGraph, name: str) -> None:
    """
    Takes in a LanguageGraph generated using our CSV data and, generates a visual repersentation of the graph using the
    Pyvis Library. Also takes in a string to name the generated file
    """
    net = Network(height="1250px", width="100%", bgcolor="#03001C", font_color="#FFF2F2")

    # Add all the Nodes
    for x in graph.get_language():
        if graph.get_language()[x].tag == "genus":
            net.add_node(n_id=graph.get_language()[x].name,
                         title=graph.get_language()[x].name,
                         color="#DDDDDD",
                         size=55,
                         label=graph.get_language()[x].name)
        elif graph.get_language()[x].tag == "major_lang":
            net.add_node(n_id=graph.get_language()[x].name,
                         title=graph.get_language()[x].name,
                         color="#A5D7E8",
                         size=25,
                         label=graph.get_language()[x].name)
        else:
            net.add_node(n_id=graph.get_language()[x].name,
                         title=graph.get_language()[x].name,
                         color="#FFDEB4",
                         size=20,
                         label=graph.get_language()[x].name)

    # Add all the Edges
    edge_color = "#57C5B6"
    for k in graph.get_language():
        for j in graph.get_language()[k].neighbours:
            net.add_edge(graph.get_language()[k].name, j.name, color=edge_color, width=3)

    net.show(name + '.html')


def highlight_path(graph: LanguageGraph, start: str, stop: str, name: str) -> None:
    """
    Takes in a LanguageGraph and a start and stop language name. Generates an interactive graph,
    that highligts the given path between the languages. Takes in the language as a string,
    assuming the languages are in the graph.

    Preconditions:
        - start in graph.get_language().keys()
        - stop in graph.get_language().keys()
        - graph.get_language()[start].find_path(stop, set()) is not None
    """
    # Last precondition ensures that there exists a path between start and stop

    net = Network(height="1250px", width="100%", bgcolor="#03001C", font_color="#FFF2F2")
    path = graph.get_language()[start].find_path(stop, set())

    # Add all the Nodes
    for x in graph.get_language():
        if graph.get_language()[x].name == start or graph.get_language()[x].name == stop:
            net.add_node(n_id=graph.get_language()[x].name,
                         title=graph.get_language()[x].name,
                         color="#DC3535",
                         size=55,
                         label=graph.get_language()[x].name)
        elif graph.get_language()[x].name in path:
            if graph.get_language()[x].tag == "genus":
                net.add_node(n_id=graph.get_language()[x].name,
                             title=graph.get_language()[x].name,
                             color="#E90064",
                             size=55,
                             label=graph.get_language()[x].name)
            elif graph.get_language()[x].tag == "major_lang":
                net.add_node(n_id=graph.get_language()[x].name,
                             title=graph.get_language()[x].name,
                             color="#E90064",
                             size=25,
                             label=graph.get_language()[x].name)
            else:
                net.add_node(n_id=graph.get_language()[x].name,
                             title=graph.get_language()[x].name,
                             color="#E90064",
                             size=20,
                             label=graph.get_language()[x].name)
        else:
            if graph.get_language()[x].tag == "genus":
                net.add_node(n_id=graph.get_language()[x].name,
                             title=graph.get_language()[x].name,
                             color="#A5D7E8",
                             size=55,
                             label=graph.get_language()[x].name)
            elif graph.get_language()[x].tag == "major_lang":
                net.add_node(n_id=graph.get_language()[x].name,
                             title=graph.get_language()[x].name,
                             color="#A5D7E8",
                             size=25,
                             label=graph.get_language()[x].name)
            else:
                net.add_node(n_id=graph.get_language()[x].name,
                             title=graph.get_language()[x].name,
                             color="#A5D7E8",
                             size=20,
                             label=graph.get_language()[x].name)

    # Add all the Edges
    edge_color = "#57C5B6"
    highlight_colour = "#E90064"
    for i in range(len(path) - 1):
        net.add_edge(path[i], path[i + 1], color=highlight_colour, width=3)

    for k in graph.get_language():
        for j in graph.get_language()[k].neighbours:
            net.add_edge(graph.get_language()[k].name, j.name, color=edge_color, width=3)

    net.show(name + '.html')


def generate_all_spanning_trees() -> None:
    """
    Generates a spanning tree for every Genus in the dataset
    """
    languages_graph = read_csv("csv/relevant_genus_languages.csv", "csv/creole_languages.csv")

    for x in languages_graph.get_language():
        if languages_graph.get_language()[x].tag == "genus":
            name = languages_graph.get_language()[x].name
            spanning_tree = languages_graph.create_spanning_tree(name)
            generate_graph(spanning_tree, "spanning_tree_" + name)

# Sample Function Calls
# languages_graph = read_csv("csv/relevant_genus_languages.csv", "csv/creole_languages.csv")
# generate_all_spanning_trees()
# generate_graph(languages_graph, "complete_graph")
# highlight_path(languages_graph, "English", "French", "english_to_french")
