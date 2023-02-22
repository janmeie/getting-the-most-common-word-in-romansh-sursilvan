#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Jana Meier

from typing import List, Tuple, Dict


def find_word(df, word: str, frequency_dictionary: Dict) -> List[Tuple[str, int]]:
    """
    accesses the dataframe and looks for the german word and its corresponding Romansh translations

    :param df: The dataframe containing the words to be extracted.
    :param word: The German word to be translated.
    :param frequency_dictionary: The dictionary containing all the words that appear in the newspaper and their frequency.
    :return: A list with tuples containing the Romansh translation and their frequency.
    """
    my_list = []
    sub_df = df.loc[df['DStichwort'] == word]
    for i, row in sub_df.iterrows():
        romansh_translation = row['RStichwort']
        if romansh_translation in frequency_dictionary:
            my_tuple = romansh_translation, frequency_dictionary[romansh_translation]
            my_list.append(my_tuple)
    final_list = list(set(my_list))
    return final_list


def get_frequent_words(final_list: List[Tuple[str, int]]) -> str:
    """sorts the types with respect to their frequency and returns the three most frequent words."""
    final_list.sort(key=lambda x: x[1], reverse=True)
    most_common_words = final_list[0:3]
    my_list = [items[0] + ':' + str(items[1]) + ' ' for items in most_common_words]
    return ''.join(my_list)
