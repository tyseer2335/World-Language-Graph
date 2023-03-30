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

    def add_language(self, name: str, tag: str) -> None:
        """Given a name, and tag of a language, add a language to the graph

        Preconditions:
        - tag in {‘major_lang’, ‘genus’, ‘creole’}
        - name != ''
        - name not in self._languages
        """
        new_language = Language(name=name, tag=tag)
        self._languages[name] = new_language

    def add_connection(self, language1: tuple[str, str], language2: tuple[str, str]) -> None:
        """Given two languages, set them as neighbours of each other in the graph. The languages
        are formatted in tuples where the first element in each tuple is the name of the language and
        the second element is its tag. Thus, if the language does not exist yet, create it.

        Preconditions:
        - language1[1] in {‘major_lang’, ‘genus’, ‘creole’} and language2[1] in {‘major_lang’, ‘genus’, ‘creole’}
        - language1[0] != '' and language2[0] != ''
        - language1[0] != language2[0]
        """

        name1, name2 = language1[0], language2[0]
        tag1, tag2 = language1[1], language2[1]

        if name1 not in self._languages:
            self.add_language(name1, tag1)
        if name2 not in self._languages:
            self.add_language(name2, tag2)

        node1, node2 = self._languages[name1], self._languages[name2]

        node1.neighbours.add(node2)
        node2.neighbours.add(node1)

    def create_spanning_tree(self, genus: str) -> LanguageGraph:
        """Create a spanning tree from a given genus and return the resulting graph

        Preconditions:
        - genus in self._languages
        """
        genus_node = self._languages[genus]
        spanning_tree_edges = genus_node.get_spanning_tree()
        spanning_tree = LanguageGraph()
        spanning_tree.add_language(genus, 'genus')

        for node1, node2 in spanning_tree_edges:
            spanning_tree.add_connection((node1.name, node1.tag), (node2.name, node2.tag))

        return spanning_tree

    def get_language(self):
        """
        Gets the languages of the LanguageGraph
        """
        return self._languages


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

    def __init__(self, name: str, tag: str) -> None:
        """Initialize this node with the given name and tag and no connections to other languages."""
        self.name = name
        self.neighbours = set()
        self.tag = tag

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
