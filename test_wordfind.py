#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Jana Meier

import pytest
import pandas as pd
from wordfind import find_word, get_frequent_words
from io import StringIO


@pytest.fixture
def df():
    name_data = StringIO('''RecID,DStichwort,RStichwort
    1,dennoch,tuttina
    2,dennoch,auncallura
    3,sprechen,discuorer
    4,sprechen,tschintschar
    5,sprechen,plidar
    6,schlafen,durmir
    7,dennoch,nuotatonmeins
    8,dennoch,tonaton''')
    names = pd.read_csv(name_data)
    return names


def test_find_word(df):
    dictionary = {'discuorer': 27, 'tschintschar': 25, 'tuttina': 25,
                  'auncallura': 11, 'nuotatonmeins': 3, 'tonaton': 20}
    result_dennoch = [('nuotatonmeins', 3), ('tuttina', 25),('auncallura', 11), ('tonaton', 20)]
    result_sprechen = [('discuorer', 27), ('tschintschar', 25)]
    assert set(find_word(df, word='dennoch', frequency_dictionary=dictionary)) == set(result_dennoch)
    assert set(find_word(df, word='sprechen', frequency_dictionary=dictionary)) == set(result_sprechen)
    assert find_word(df, word='schlafen', frequency_dictionary=dictionary) == []
    assert type(find_word(df, word='dennoch', frequency_dictionary=dictionary)) == list
    assert len(find_word(df, word='dennoch', frequency_dictionary=dictionary)) != 0


def test_frequent_word():
    input_dennoch = [('auncallura', 11), ('nuotatonmeins', 3), ('tuttina', 25), ('tonaton', 20)]
    input_sprechen = [('discuorer', 27), ('tschintschar', 25)]
    assert get_frequent_words(input_dennoch) == 'tuttina:25 tonaton:20 auncallura:11 '
    assert get_frequent_words(input_sprechen) == 'discuorer:27 tschintschar:25 '
    assert type(get_frequent_words(input_dennoch)) == str