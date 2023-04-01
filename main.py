"""This Python file contains the main classes we need for our assignment"""


from __future__ import annotations

class LanguageGraph:
    """A graph representing the connections between various languages.

    Representation Invariants:
    - all(name == self._languages[name].name for name in self._languages)
    """
    # Private Instance Attributes:
    #     - _languages: A collection of the languages contained in this graph.
    #                  Maps the name of the language to Language instance.
    _languages: dict[str, Language]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._languages = {}

    def get_node(self, name):
        """Given the name of the language node, give the actual node

        Preconditions:
        - name in self._languages
        """
        return self._languages[name]

    def add_language(self, language: Language) -> None:
        """Given a name of language and a tag, add a language to the graph

        Preconditions:
        - tag in {‘major_lang’, ‘genus’, ‘creole’}
        - name != ''
        - name not in self._languages
        """
        self._languages[language.name] = language

    def add_connection(self, language1: Language, language2: Language) -> None:
        """Given two languages, set them as neighbours of each other in the graph. The languages
        are formatted in tuples where the first element in each tuple is the name of the language and
        the second element is its tag. Thus, if the language does not exist yet, create it.

        Preconditions:
        - language1[1] in {‘major_lang’, ‘genus’, ‘creole’} and language2[1] in {‘major_lang’, ‘genus’, ‘creole’}
        - language1[0] != '' and language2[0] != ''
        - language1[0] != language2[0]
        """


        if language1.name not in self._languages:
            self.add_language(language1)
        if language2.name not in self._languages:
            self.add_language(language2)

        language1.neighbours.add(language2)
        language2.neighbours.add(language1)

    def create_spanning_tree(self, genus: str) -> LanguageGraph:
        """Create a spanning tree from a given genus and return the resulting graph

        Preconditions:
        - genus in self._languages
        """
        genus_node = self._languages[genus]
        spanning_tree_edges = genus_node.get_spanning_tree()
        spanning_tree = LanguageGraph()
        genus_node = Language(genus, 'genus', '')
        spanning_tree.add_language(genus_node)

        for node1, node2 in spanning_tree_edges:
            spanning_tree.add_connection(node1, node2)

        return spanning_tree

    def find_paths(self, start: str, end: str) -> list[LanguageGraph]:
        """Return a list of all paths in this network, with each path represented as a linear graph.

        Preconditions:
            - start in self._nodes
            - end in self._nodes

        """
        start_node = self._languages[start]
        paths = start_node.find_paths(end, set())


        graphs = []
        for path in paths:
            # print([node.name for node in path])
            new_graph = LanguageGraph()
            for i in range(len(path) - 1):
                node1, node2 = path[i], path[i + 1]
                new_graph.add_connection(node1, node2)
            graphs.append(new_graph)
        return graphs

    def location_based_graph(self, area: str) -> LanguageGraph:
        """Return a graph of all the genuses/languages/creoles for a given location

        Preconditions:
        - area is a valid macroarea from the csv file
        """
        new_graph = LanguageGraph()
        for language in self._languages:
            lang_node = self._languages[language]
            if lang_node.area == area:
                new_graph.add_language(lang_node)
                for neighbour in lang_node.neighbours:
                    new_graph.add_connection(lang_node, neighbour)
        return new_graph

    def creole_based_graph(self, creole: str) -> LanguageGraph:
        """Return a tree like graph with all the languages/genuses connected to a given creole

        Preconditions:
        - creole in self._languages
        """
        new_graph = LanguageGraph()
        creole_node = self._languages[creole]
        for lang_node in creole_node.neighbours:
            genus_node = lang_node.find_genus()
            new_graph.add_connection(lang_node, genus_node)
            new_graph.add_connection(lang_node, creole_node)
        return new_graph


class Language:
    """A node that represents a language in our graph.

    Instance Attributes
    - name:
        The name of the language (e.g. English, French)
    - neighbours:
        The languages that are neighbours with this one. This is through a parental relationship from genus or
        from language to creole
    - tag:
        Indicates whether this is a genus, major language, or creole
    - area:
        The macroarea in which the language is found

    Representation Invariants:
    - self not in self.neighbours
    - all(self in neighbour.neighbours for neighbour in self.neighbours)
    - self.tag != ‘creole’ or all(neighbour.tag != ‘creole’ for neighbour in self.neighbours)
    - self.tag in {‘major_lang’, ‘genus’, ‘creole’}
    """
    # the second last invariant is stating that creoles cannot be connected to other creoles
    name: str
    neighbours: set[Language]
    tag: str
    area: str
    def __init__(self, name: str, tag: str, area: str) -> None:
        """Initialize this node with the given name and tag and no connections to other languages."""
        self.name = name
        self.neighbours = set()
        self.tag = tag
        self.area = area

    def get_spanning_tree(self) -> list[set]:
        """Return a spanning tree for all languages/creoles that derive from the node

        Preconditions:
        - self.tag == 'genus'
        """
        edges_so_far = []
        for language in self.neighbours:
            edges_so_far.append({self, language})
            for neighbour in language.neighbours:
                if neighbour.tag != 'genus':
                    edges_so_far.append({language, neighbour})
        return edges_so_far

    def find_paths(self, destination: str, visited: set[Language]) -> list[list[Language]]:
        """Return a list of all possible paths from this vertex that do NOT use any nodes in visited.

        The paths may be returned in any order. NOTE: unlike lecture, where paths were defined as a
        sequence of vertices, here a path is defined as a sequence of Channels (i.e., edges). This
        representing a bit more helpful for this assignment.
        """
        if self.name == destination:
            return [[self]]
        paths = []
        visited = visited.union({self})
        for neighbour in self.neighbours:
            if neighbour not in visited:
                new_paths = neighbour.find_paths(destination, visited)
                for path in new_paths:
                    paths.append([self] + path)
        return paths

    def find_genus(self) -> Language:
        """Given a language, find its respective genus

        Preconditions:
        - self.tag == 'major_lang'
        """
        for neighbour in self.neighbours:
            if neighbour.tag == 'genus':
                return neighbour
