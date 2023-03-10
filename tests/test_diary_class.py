from lib.diary_class import Diary
from lib.diary_entry_class import DiaryEntry
import pytest


"""

UNIT TESTS FOR DIARY CLASS ONLY

"""

"""


Diary class is used to hold and manipulate DiaryEntry type objects
uses to add structure to the various functions within DiaryEntry


It has one local variable  - a list of entries

It has 5 methods

1. add - adds a new diary entry
    parameters - 1, the entry
    no return
    adds to the list of entries

2. all - lists diary entriers
    parameters - none
    returns list of diary entries (just titles?)
    doesnt manipulate the data

3. count_words - lists quantity of words in all entries contained
    parameeters - none
    returns - int, number of words in all entries
    uses count_words method within DiaryEntry

4. reading_time - determines a reading time for all entries in the diary
    paramteres - 1 - wpm
    returns = integer, representing minutes or seconds taken to read

5. find_best_entry_for_reading_time - most complex one
gives the diary entry chunk that is clossest to the given time, given wpm and monutes

    parameters - wpm and minutes
    returns - an entry, both title and contents?


"""

"""

NOTES - almost no functions can be tested alone without using integrated tests

"""

#tests that a list is created when diary is

def test_list_created():
    test_diary = Diary()

    assert test_diary.entry_list == []

#tests that all other functions return an error if no entries given

def test_for_no_entries():
    test_diary = Diary()

    with pytest.raises(Exception) as e:
        test_diary.all()
    error_message_all = str(e.value)

    with pytest.raises(Exception) as e:
        test_diary.count_words()
    error_message_count_words = str(e.value)

    with pytest.raises(Exception) as e:
        test_diary.reading_time(20)
    error_message_reading_time = str(e.value)

    with pytest.raises(Exception) as e:
        test_diary.find_best_entry_for_reading_time(20,20)
    error_message_find_best_entry_for_reading_time = str(e.value)

    assert error_message_all == "No entries!"
    assert error_message_count_words == "No entries!"
    assert error_message_reading_time == "No entries!"
    assert error_message_find_best_entry_for_reading_time == "No entries!"


    

