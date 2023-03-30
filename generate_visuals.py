"""This Python file genrates the visulizations from the Graph"""
from main import LanguageGraph
from pyvis.network import Network
from csv_reader import read_csv


def generate_visuals(graph: LanguageGraph, name: str) -> None:
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
    edge_color = "#2F58CD"
    for k in graph.get_language():
        for j in graph.get_language()[k].neighbours:
            net.add_edge(graph.get_language()[k].name, j.name, color=edge_color, width=3)

    net.show(name + '.html')

# Sample Function Call
# languages_graph = read_csv("csv/relevant_genus_languages.csv", "csv/creole_languages.csv")
# generate_visuals(languages_graph, "completed_visuals")
