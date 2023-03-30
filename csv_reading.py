import csv
from main import LanguageGraph


def read_csv(language_csv: str, creole_csv: str) -> LanguageGraph:
    """Take in 2 files containing a list of all the languages and a list of all the creoles respectively
    and return a LanguageGraph populated with them

    Preconditions:
    - for every row in language_csv, the 4th column is the language and the 7th is the genus
    - for every row in creole_csv, the 1st column is the creole and the 2nd is the contributing languages

    """
    language_graph = LanguageGraph()

    with open(language_csv) as lang_file:
        with open(creole_csv) as creole_file:
            lang_reader = list(csv.reader(lang_file))[1:]
            creole_reader = list(csv.reader(creole_file))[1:]
            languages_set = {row[3] for row in lang_reader}
            for row in lang_reader:
                language, genus = row[3], row[6]
                language_graph.add_connection((language, 'major_lang'), (genus, 'genus'))
            for name, contributors in creole_reader:
                contributors = contributors.split(', ')

                if all(lang in languages_set for lang in contributors):
                    for contributor in contributors:
                        language_graph.add_connection((contributor, 'major_lang'), (name, 'creole'))
    return language_graph

# testing
#
# a = read_csv('csv/relevant_genus_languages.csv', 'csv/creole_languages.csv')
#
# node = a._languages['Germanic']
#
# tree = a.create_spanning_tree('Germanic')
# for lang in tree._languages:
#     print(lang)
# # print('\n\n')
# # print(len(tree._languages))
# # print(len(node.neighbours))
# #
# # for lang_node in node.neighbours:
# #     # for neighbor in lang_node.neighbours:
# #     #     if neighbor.tag != 'genus':
# #     #         print(neighbor.name)
# #     print(lang_node.name)
