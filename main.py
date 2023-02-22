#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Jana Meier

"""
Find the three most used Romansh translations of a German word.
"""
from argparse import ArgumentParser

import pandas as pd
import glob
import os
import pickle

from text_utils import get_tokenized_words, get_word_dictionary
from wordfind import find_word, get_frequent_words


def get_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(description='Find the three most used Romansh translation of a German word.')
    parser.add_argument('word', type=str,
                        help='The word to be translated.')
    return parser


def create_dict_file() -> None:
    """
    Calls a function to create a dictionary with the Romansh words and their frequency if it is not already available.
    """
    print('Creating dictionary file...')
    input_path = 'data/La_Quotidiana_txt'
    file_list = glob.glob(os.path.join(input_path, '*.txt'))
    total_list = []
    for files in file_list:
        infile = open(files, 'r', encoding='utf-8')
        # Get tokens in the newspaper
        processed_list = get_tokenized_words(infile)
        total_list.extend(processed_list)
    # Get the frequency of each lemma that appears in the newspaper
    word_dictionary = get_word_dictionary(total_list)
    dict_file = open('data/word_dictionary.pkl', 'wb')
    pickle.dump(word_dictionary, dict_file)
    dict_file.close()


def main():
    parser = get_argument_parser()
    args = parser.parse_args()
    print('Looking for translations of: '+args.word+'...' )
    # If there is no word_dictionary create one
    if not os.path.exists('data/word_dictionary.pkl'):
        create_dict_file()
    dict_file = open('data/word_dictionary.pkl', 'rb')
    word_dictionary = pickle.load(dict_file)
    df = pd.read_csv('data/NVS-sco-PG_A-Z.csv')
    # Get the Romansh translations of a German word
    extract_word_csv = find_word(df, args.word, word_dictionary)
    # Get the three most common translations and print them with respect to their frequency
    if not extract_word_csv:
        print('sorry, the word was not found')
    else:
        frequent_words = get_frequent_words(extract_word_csv)
        print(args.word, '>', frequent_words)


if __name__ == '__main__':
    main()