"""
===============================
This module contains the functions that read in the CSV data, and converts it into a LanuageGraph
===============================
Copyright and Usage Information
===============================
This file is Copyright (c) 2023 Tyseer Toufiq, Michael Zhao, Varun Sahni and Dexter Tam
"""
import csv
from language import Language, LanguageGraph


def read_csv(language_csv: str, creole_csv: str) -> LanguageGraph:
    """Take in 2 files containing a list of all the languages and a list of all the creoles respectively
    and return a LanguageGraph populated with them

    Preconditions:
    - for every row in language_csv, the 4th column is the language, the 7th is the genus and the 9th is the area
    - for every row in creole_csv, the 1st column is the creole and the 2nd is the contributing languages
    """
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


# if __name__ == '__main__':
#     import python_ta
#
#     python_ta.check_all(config={
#         'max-line-length': 120,
#         'disable': ['E9999'],
#         'allowed-io': ['read_csv']
#     })
