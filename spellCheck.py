#!/usr/bin/env python
__author__ = "Yadollah Shahryary Dizaji"
__title__ = "setup.py"
__description__ = "NLP for spell checking"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "shahryary@gmail.com"


import os

from symspellpy.symspellpy import SymSpell, Verbosity  # import the module


def main():
    # maximum edit distance per dictionary precalculation
    max_edit_distance_dictionary = 2
    prefix_length = 7
    # create object
    sym_spell = SymSpell(max_edit_distance_dictionary, prefix_length)
    # load dictionary
    dictionary_path = os.path.join(os.path.dirname(__file__),
                                   "frequency_dictionary_en_82_765.txt")
    term_index = 0  # column of the term in the dictionary text file
    count_index = 1  # column of the term frequency in the dictionary text file
    if not sym_spell.load_dictionary(dictionary_path, term_index, count_index):
        print("Dictionary file not found")
        return

    sym_spell.load_dictionary("/home/yadi/projectDISK/Python-Projects/ML-NLP/dictionary.txt", 0, 1)


    # lookup suggestions for multi-word input strings (supports compound
    # splitting & merging)
    input_term = ("whereis th elove hehad dated forImuch of thepast who "
                  "couqdn'tread in sixtgrade and ins pired him."
                  "I'm workig in th e yadolah shahrary working in githib")
    # max edit distance per lookup (per single word, not per whole input string)
    max_edit_distance_lookup = 1
    suggestions = sym_spell.lookup_compound(input_term,
                                            max_edit_distance_lookup,transfer_casing=True)
    # display suggestion term, edit distance, and term frequency
    print(input_term)
    for suggestion in suggestions:
        print("{}".format(suggestion.term))


if __name__ == "__main__":
    main()