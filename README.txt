GETTING THE MOST COMMON WORD IN ROMANSH SURSILVAN

Find the three most used Romansh translations of a German word.


1. Introduction

Sursilvan is one of the five spoken Romansh languages in the Grisons. There is an online dictionary
'Niev Vocabulari Sursilvan Online' (www.vocabularisursilvan.ch) in which you can enter a word in German
or Sursilvan and it will return the respective translations. But this dictionary has the disadvantage
that it sorts its output alphabetically and not according to its frequency. This is inconvenient given
that especially in the beginning, language learners use a rather basic vocabulary, mostly words which
occur very often.

Example: if you want to look for the translation of 'essen', the dictionary gives the full extension
of 'essen' (to nosh, to chomp, to nibble, to dine, …). For new learners it is sometimes impossible to
choose the most common word out of this giant list.

The aim of this program is to help language learners to get the most common word in Sursilvan.


2. Usage

In order to get the Romansh translation of a German word (only lemmas: e.g. no conjugated verbs
and no plural nouns), the following input is required:

    python main.py word

An example is the following:

    python main.py sprechen

The output contains the German word and the corresponding Romansh translation accompanied and ordered
by their frequency:

    sprechen > tschintschar:11 discuorer:11 plidar:2

3. Data

Unfortunately, I cannot share the data.

The data folder contains a collection of pdf documents of the newspaper 'La Quotidiana', written in
Romansh, which I converted to a text document in order to count how often each word appears. The
translation that appears the most, is considered to be the most common one. I did the conversion with
pdfminer. The python program for the conversion is in the directory 'preprocessing' and the converted
text files are in the data folder.
Note: Since the pdf documents have the typical newspaper layout, I could not keep the original sequence
(the converter does not start with the most left column but with the highest). Therefore, I deleted all
hyphenated words because it is not always the case that the next line belongs to the previous line. Hence,
my data is slightly biased towards short words. Additionally, I removed all capitalized words, because
they contain metadata information like name of the author or of the newspaper and the date. I also removed
digits and punctuation because they are not of interest.

The data folder also holds a xlsx file, which contains German words and their Romansh translation.
Lia Rumantscha, an organization that promotes Romansh language, provided me this xlsx document, which
the online dictionary 'Niev Vocabulari Sursilvan Online' is based on. I converted the xlsx document to
a csv file, in order to access the table. The goal was to extract the Romansh translations from the
excel document. Then, the program counts how often each of the translations appears in the text document
and sorts them based on their frequency of occurrence. The csv file is also in the data folder and the
converter in the preprocessing directory.
Note: this file must not be send to third parties and can only be used for this project, those are the
conditions of Lia Rumantscha.

My program has some limitations. One of the issues is that the program can not look for inflected words but
only for lemmas (basic forms) because the dictionary data does not contain conjugations for verbs and feminine
and plural forms for adjective and nouns. Another problem occurs with homonyms, words with more than one meaning.
Since I do not work with translated texts, my program is not able to only count the intended translation of
the German word. Finally, another issue is that my corpus is not large enough, therefore it does not contain
all words that are in the online dictionary.


4. References

Alekseev, Pavel (2008): “Frequency dictionaries”, in: Reinhard Köhler, Gabriel Altmann & Rajmund G. Piotrowski (eds.),
Quantitative Linguistik / Quantitative Linguistics: Ein Internationales Handbuch / an International Handbook.
Berlin/Boston: De Gruyter, 312-324.



