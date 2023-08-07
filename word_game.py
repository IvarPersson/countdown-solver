"""
Word generator used in the word game in the british TV-show Countdown
"""

import itertools
import pickle
from typing import Union


class WordGameCalculator:
    """
    Finds the best words given its inputs
    """

    def __init__(self) -> None:
        self.types = [
            "prefix",
            "abbr.",
            "n.",
            "adv.",
            "predic.",
            "adj.",
            "naut.",
            "v.",
            "gram.",
            "suffix",
            "(also",
            "prep.",
            "int.",
            "comb.",
            "symb.",
            "contr.",
            "colloq.",
            "conj.",
            "attrib.",
            "var.",
            "past of",
            "see",
            "pl.",
            "(pl.",
            "past part.",
            "past",
            "archaic",
            "compar.",
            "superl.",
            "pres.",
            "part. of",
            "objective case",
        ]
        self.strip_chars = " \t\n0123456789"
        self.dictionary_path = "./dictionary.txt"

    def _test_words(self, words: list):
        true_words = []
        with open("dictionary.pkl", "rb") as pkl_file:
            dictionary = pickle.load(pkl_file)
        for word in words:
            if word in dictionary:
                true_words.append(word)
        return true_words

    def read_dictionary(self):
        """
        Reads the dictionary file and stores it as a dictionary with words as keys and description
        as value.
        """
        dictionary_dict = {}
        trimmed = 0
        dictionary_dict[
            "usage"
        ] = "n. 1 use, treatment (damaged by rough usage). \
                2 customary practice, esp. In the use of a language\
                or as creating a precedent in law."
        with open(self.dictionary_path, "r", encoding="utf8") as dic_file:
            lines = dic_file.readlines()
            for line in lines:
                line = line.lower().strip(self.strip_chars)
                if line.startswith("usage") or line == "":
                    continue
                if line == "\n":
                    continue
                idx_list = []
                for typ in self.types:
                    tmp = line.find("—" + typ)
                    if tmp != -1:
                        idx_list.append(tmp)
                        continue
                    tmp = line.find(typ)
                    if tmp != -1:
                        idx_list.append(tmp)
                if not idx_list:
                    continue
                idx = min(idx_list)
                if idx > 20:  # type: ignore
                    continue
                word = line[:idx].strip(self.strip_chars)
                if " " in word or len(word) > 9:
                    trimmed += 1
                    continue
                meaning = line[idx:].strip(self.strip_chars)
                dictionary_dict[word] = meaning
        with open("dictionary.pkl", "wb") as pkl_file:
            pickle.dump(dictionary_dict, pkl_file)
        print(
            f"Successfully read: {len(dictionary_dict.keys())} words from the dictionary."
        )
        print(f"{trimmed} words were removed due to reasons")

    def generate_true_words(self, letters: Union[list, str]):
        """
        Prints the true words of the letter list
        """
        true_words_dict = {}
        if isinstance(letters, str):
            letters = list(letters)
        letters = list(letters)
        for nbr_letters in range(9, 2, -1):
            letter_list = list(itertools.combinations(letters, nbr_letters))
            letter_list = [list(let) for let in letter_list]
            words = []
            for letter_comb in letter_list:
                words += [
                    "".join(tup) for tup in list(itertools.permutations(letter_comb))
                ]
            true_words = self._test_words(set(words))  # type: ignore
            true_words_dict[f"{str(nbr_letters)}"] = true_words
        return true_words_dict
