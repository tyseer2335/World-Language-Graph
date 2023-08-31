import csv
from language import Language, LanguageGraph


def read_csv(language_csv: str, creole_csv: str) -> LanguageGraph:
    language_graph = LanguageGraph()

    with open(language_csv) as lang_file:
        with open(creole_csv) as creole_file:
            lang_reader = list(csv.reader(lang_file))[1:]
            creole_reader = list(csv.reader(creole_file))[1:]
            languages_set = set()
            for row in lang_reader:
                languages_set.add(row[3])
                lang_node = Language(row[3], 'major_lang', row[8])
                genus_node = Language(row[6], 'genus', '')
                language_graph.add_connection(lang_node, genus_node)

            for name, contributors in creole_reader:

                contributors = contributors.split(', ')

                if all(lang in languages_set for lang in contributors):
                    creole_node = Language(name, 'creole', '')
                    for contributor in contributors:
                        language_graph.add_connection(language_graph.get_node(contributor), creole_node)
    return language_graph