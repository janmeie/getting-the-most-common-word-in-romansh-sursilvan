#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Jana Meier

import re
from nltk.tokenize import word_tokenize
from typing import TextIO, Dict, List


def get_tokenized_words(file: TextIO) -> List[str]:
    """Clean a text and convert it into a list of token"""
    token_list = []
    punctuation = '!()[]{}«»;:"\\,<>./?@#$%^&*_~'
    line_with_hyphen = False
    for lines in file:
        # Subtract hyphenated words
        clean_lines = re.sub(r'\w+-$', '', lines)
        # Subtract digits
        clean_lines = re.sub(r'\d+', '', clean_lines)
        # Subtract capitalized words
        clean_lines = re.sub(r'\b[A-Z]+\b', '', clean_lines)
        # Subtract apostrophe
        clean_lines = re.sub(r'’', ' ', clean_lines)
        # Lower characters
        clean_lines = clean_lines.lower()
        for element in clean_lines:
            # Subtract punctuation
            if element in punctuation:
                clean_lines = clean_lines.replace(element, '')
        # Tokenize the lines
        tokenized_words = word_tokenize(clean_lines)
        # if the previous line ended with a hyphen, delete the first element of the current line
        if line_with_hyphen and len(tokenized_words) > 0:
            tokenized_words.pop(0)
        # Store true for the current line if it ends with a hyphen
        if re.search(r'\w+-$', lines):
            line_with_hyphen = True
        else:
            line_with_hyphen = False
        token_list.extend(tokenized_words)
    return token_list


def get_word_dictionary(token_list: List[str]) -> Dict[str, int]:
    """Get the number of each tokens."""
    counts = dict()
    for word in token_list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
