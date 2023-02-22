#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Jana Meier

import io
from text_utils import get_tokenized_words, get_word_dictionary



def test_tokenized_words():
    newspaper_input = io.StringIO('THIS IS \na test \n12. Mai 2021 \n«This. is a test» \nDoes hypheni-\nsation work?')
    assert get_tokenized_words(newspaper_input) == ['a', 'test', 'mai', 'this', 'is', 'a', 'test', 'does', 'work']
    assert type(get_tokenized_words(newspaper_input)) == list
    assert type(get_tokenized_words(newspaper_input)) != 0
    assert get_tokenized_words(io.StringIO('Does hypheni-\nsation work?')) == ['does', 'work']
    assert get_tokenized_words(io.StringIO('12.')) == []
    assert get_tokenized_words(io.StringIO('CAPITALISATION')) == []
    assert get_tokenized_words(io.StringIO('d’Amélie')) == ['d', 'amélie']
    assert get_tokenized_words(io.StringIO('Test')) == ['test']
    assert get_tokenized_words(io.StringIO('"[Punctuation]!?"')) == ['punctuation']
    assert get_tokenized_words(io.StringIO('hypheni-\nsation')) == []


def test_word_dictionary():
    list_input = ['a', 'test', 'mai', 'this', 'is', 'a', 'test', 'does', 'work']
    assert get_word_dictionary(list_input) == {'a': 2, 'test': 2, 'mai': 1, 'is': 1, 'does': 1, 'this': 1, 'work': 1}
    assert type(get_word_dictionary(list_input)) == dict
    assert len(get_word_dictionary(list_input)) != 0