from lib.diary_class import Diary
from lib.diary_entry_class import DiaryEntry
import pytest




"""

UNIT TESTS FOR DIARY ENTRY CLASS ONLY

"""

"""

DiaryEntry class is used to contain and format data, in the form of entrie

each instance has two local variables = title and contents

there are three methods:

1.count words - returns the quantity of words in the contents

2. reading time - uses wpm to calculate time to read contents

3. reading chunk - uses reading_time and given minutes to calculate
a chunk of text the reader has time to read. also loops

"""


"""
KNOWN ISSUES - when initialising a diary entry, there are no checks for format
or type, it will break if anything other than a string given
"""


#tests to see if the title and contents are saved as local variables in the instance

def test_check_title_and_contents():
    test_entry = DiaryEntry("Title", "Contents")

    assert test_entry.title == "Title"
    assert test_entry.contents == "Contents"

#checks to see if count_words counts correctly

def test_check_count_words_accurate():
    test_entry = DiaryEntry("Title", "This is sample text")

    assert test_entry.count_words() == 4

#checks to see if count words works even with breaks and spaces

def test_check_count_words_accurate():
    test_entry = DiaryEntry("Title", " This is sample text ")
    test_entry2 = DiaryEntry("Title", "a     a")
    test_entry3 = DiaryEntry("Title", " ")

    assert test_entry.count_words() == 4
    assert test_entry2.count_words() == 2
    assert test_entry3.count_words() == 0

#checks to see if reading time calculates correctly

def test_check_reading_time_correct():

    test_entry = DiaryEntry("13/13/2030", "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of  (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, , comes from a line in section 1.10.32.")

    assert test_entry.count_words() == 120
    assert test_entry.reading_time(60) == 2
    assert test_entry.reading_time(60.0) == 2
    assert test_entry.reading_time(30) == 4

#checks the various functions of reading chunk, including size, formatting and looping

def test_reading_chunk():

    entry = DiaryEntry("13/13/2040", "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of  (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, , comes from a line in section 1.10.32.")

    #when called, returns the two arguments times together # of words

    assert entry.reading_chunk(5,2) == "Contrary to popular belief, Lorem Ipsum is not simply random"

    # when called again on the same instance, returns the same but starting
    # from where the previous return left off

    assert entry.reading_chunk(5,2) == "text. It has roots in a piece of classical Latin"

    # when called multiple times, loops back round to the start of the stext

    entry_2 = DiaryEntry("10/10/1349", "Caught the plague. Again. Why do I keep catching plague.")

    assert entry_2.reading_chunk(4,2) == "Caught the plague. Again. Why do I keep"
    assert entry_2.reading_chunk(4,2) == "catching plague. Caught the plague. Again. Why do"

    entry_3 = DiaryEntry("Hello", "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur,")

    assert entry_3.reading_chunk(4,10) == "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia,"
    assert entry_3.reading_chunk(4,10) == "looked up one of the more obscure Latin words, consectetur, Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."