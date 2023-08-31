from __future__ import annotations
from typing import Optional


class LanguageGraph:
    _languages: dict[str, Language]

    def __init__(self) -> None:
        self._languages = {}

    def get_node(self, name: str) -> Language:
        return self._languages[name]

    def add_language(self, language: Language) -> None:
        self._languages[language.name] = language

    def add_connection(self, language1: Language, language2: Language) -> None:
        if language1 is not None and language2 is not None:
            if language1.name not in self._languages:
                self.add_language(language1)
            if language2.name not in self._languages:
                self.add_language(language2)

            language1, language2 = self._languages[language1.name], self._languages[language2.name]

            language1.neighbours.add(language2)
            language2.neighbours.add(language1)
        else:
            return

    def create_spanning_tree(self, genus: str) -> LanguageGraph:
        genus_node = self._languages[genus]
        spanning_tree_edges = genus_node.get_spanning_tree()
        spanning_tree = LanguageGraph()
        genus_node = Language(genus, 'genus', '')
        spanning_tree.add_language(genus_node)

        for node1, node2 in spanning_tree_edges:
            spanning_tree.add_connection(node1, node2)

        return spanning_tree

    def get_language(self) -> dict[str, Language]:
        return self._languages

    def location_based_graph(self, area: str) -> LanguageGraph:
        new_graph = LanguageGraph()
        for language in self._languages:
            lang_node = self._languages[language]
            if lang_node.area == area:
                new_graph.add_language(lang_node)
                for neighbour in lang_node.neighbours:
                    new_graph.add_connection(lang_node, neighbour)
        return new_graph

    def creole_based_graph(self, creole: str) -> LanguageGraph:
        new_graph = LanguageGraph()
        creole_node = self._languages[creole]
        for lang_node in creole_node.neighbours:
            genus_node = lang_node.find_genus()
            new_graph.add_connection(lang_node, genus_node)
            new_graph.add_connection(lang_node, creole_node)
        return new_graph


class Language:
    name: str
    neighbours: set[Language]
    tag: str
    area: str

    def __init__(self, name: str, tag: str, area: str) -> None:
        self.name = name
        self.neighbours = set()
        self.tag = tag
        self.area = area

    def get_spanning_tree(self) -> list[set]:
        edges_so_far = []
        for language in self.neighbours:
            edges_so_far.append({self, language})
            for neighbour in language.neighbours:
                if neighbour.tag != 'genus':
                    edges_so_far.append({language, neighbour})
        return edges_so_far

    def find_genus(self) -> Optional[Language]:
        for neighbour in self.neighbours:
            if neighbour.tag == 'genus':
                return neighbour
        return None

    def find_path(self, target_item: str, visited: set[Language]) -> Optional[list]:
        if self.name == target_item:
            return [self.name]
        else:
            visited.add(self)
            return self._find_path_helper(target_item, visited)

    def _find_path_helper(self, target_item: str, visited: set[Language]) -> Optional[list]:
        for u in self.neighbours:
            if u not in visited:
                path = u.find_path(target_item, visited)
                if path is not None:
                    return [self.name] + path
        return None


