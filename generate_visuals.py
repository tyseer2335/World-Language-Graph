from pyvis.network import Network
from language import LanguageGraph
from csv_reader import read_csv


def generate_graph(graph: LanguageGraph, name: str) -> None:
    net = Network(height="1250px", width="100%", bgcolor="#03001C", font_color="#FFF2F2")
    nodes = []
    langs = graph.get_language()

    # Add all the Nodes
    for x in langs:
        if langs[x].tag == "genus":
            nodes.append(langs[x].name)
            net.add_node(n_id=langs[x].name,
                         title=langs[x].name,
                         color="#DDDDDD",
                         size=55,
                         label=langs[x].name)
        elif graph.get_language()[x].tag == "major_lang":
            nodes.append(langs[x].name)
            net.add_node(n_id=langs[x].name,
                         title=langs[x].name,
                         color="#A5D7E8",
                         size=25,
                         label=langs[x].name)
        else:
            nodes.append(langs[x].name)
            net.add_node(n_id=langs[x].name,
                         title=langs[x].name,
                         color="#FFDEB4",
                         size=20,
                         label=langs[x].name)

    # Add all the Edges
    edge_color = "#57C5B6"
    for k in langs:
        for j in langs[k].neighbours:
            if langs[k].name in nodes and j.name in nodes:
                net.add_edge(langs[k].name, j.name, color=edge_color, width=3)
    net.show(name + '.html')


def highlight_path(graph: LanguageGraph, start: str, stop: str, name: str) -> None:
    net = Network(height="1250px", width="100%", bgcolor="#03001C", font_color="#FFF2F2")
    langs = graph.get_language()
    path = langs[start].find_path(stop, set())
    nodes = []

    # Add all the Nodes
    for x in langs:
        if langs[x].name in {start, stop}:
            nodes.append(langs[x].name)
            net.add_node(n_id=langs[x].name,
                         title=langs[x].name,
                         color="#DC3535",
                         size=55,
                         label=langs[x].name)
        elif langs[x].tag == "genus" and langs[x].name in path:
            nodes.append(langs[x].name)
            net.add_node(n_id=langs[x].name,
                         title=langs[x].name,
                         color="#E90064",
                         size=55,
                         label=langs[x].name)
        elif langs[x].tag == "major_lang" and langs[x].name in path:
            nodes.append(langs[x].name)
            net.add_node(n_id=langs[x].name,
                         title=langs[x].name,
                         color="#E90064",
                         size=25,
                         label=langs[x].name)
        elif langs[x].tag == "creole" and langs[x].name in path:
            nodes.append(langs[x].name)
            net.add_node(n_id=langs[x].name,
                         title=langs[x].name,
                         color="#E90064",
                         size=20,
                         label=langs[x].name)
        else:
            if langs[x].tag == "genus":
                nodes.append(langs[x].name)
                net.add_node(n_id=langs[x].name,
                             title=langs[x].name,
                             color="#A5D7E8",
                             size=55,
                             label=langs[x].name)
            elif langs[x].tag == "major_lang":
                nodes.append(langs[x].name)
                net.add_node(n_id=langs[x].name,
                             title=langs[x].name,
                             color="#A5D7E8",
                             size=25,
                             label=langs[x].name)
            else:
                nodes.append(langs[x].name)
                net.add_node(n_id=langs[x].name,
                             title=langs[x].name,
                             color="#A5D7E8",
                             size=20,
                             label=langs[x].name)

    # Add all the Edges
    edge_color = "#57C5B6"
    highlight_colour = "#E90064"
    for i in range(len(path) - 1):
        net.add_edge(path[i], path[i + 1], color=highlight_colour, width=3)

    for k in langs:
        for j in langs[k].neighbours:
            if langs[k].name in nodes and j.name in nodes:
                net.add_edge(langs[k].name, j.name, color=edge_color, width=3)

    net.show(name + '.html')


def generate_all_graphs() -> None:
    """
    Generates every possilbe, spanning tree, creole based graph, and location based graph
    """
    languages_graph = read_csv("csv/relevant_genus_languages.csv", "csv/creole_languages.csv")
    langs = languages_graph.get_language()

    for x in langs:
        if langs[x].tag == "genus":
            name = langs[x].name
            spanning_tree = languages_graph.create_spanning_tree(name)
            generate_graph(spanning_tree, "generated_graph")

    areas = []
    for x in langs:
        areas.append(langs[x].area)
    for x in set(areas):
        area_graph = languages_graph.location_based_graph(x)
        generate_graph(area_graph, "generated_graph")

    for x in langs:
        if langs[x].tag == "creole":
            name = langs[x].name
            if name is not None:
                creole_graph = languages_graph.creole_based_graph(name)
                generate_graph(creole_graph, "generated_graph")


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['E9999']
    })

# Sample Function Calls
# languages_graph = read_csv('csv/relevant_genus_languages.csv', 'csv/creole_languages.csv')
# generate_graph(languages_graph, "complete_graph")
# highlight_path(languages_graph, "English", "French", "english_to_french")
# generate_all_graphs()
