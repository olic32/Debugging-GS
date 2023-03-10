from lib.diary_class import Diary
from lib.diary_entry_class import DiaryEntry
import pytest


"""

INTEGRATION TESTS!

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

#test that both functions are accesible to the test suite

def test_test():
    test_diary = Diary()

    assert test_diary.entry_list == []

    test_entry = DiaryEntry("Title","Contents")

    assert test_entry.title == "Title"
    assert test_entry.contents == "Contents"

#test that an entry can be addded to the local list

def test_add_and_show():
    test_diary = Diary()
    test_entry = DiaryEntry("Title","Contents")

    test_diary.add(test_entry)

    assert test_diary.entry_list == [test_entry]

#test that only entry format objects can be added - otherwise error

def test_add_wrong_data():
    test_diary = Diary()
    test_entry_wrong_data = [1,2,3]

    with pytest.raises(Exception) as e:
        test_diary.add(test_entry_wrong_data)
    error_message = str(e.value)
    assert error_message == "Cannot add non-entries to diary!"

#Test that when multiple entries are added, they are all within the list

def test_multiple_entries():
    test_diary = Diary()
    test_entry = DiaryEntry("Title","Contents")
    test_entry_2 = DiaryEntry("Title_2","Contents_2")

    test_diary.add(test_entry)
    test_diary.add(test_entry_2)

    assert test_diary.entry_list == [test_entry,test_entry_2]

#test that when mutliple entries are added, they are returned by the all function

def test_all_show():
    test_diary = Diary()
    test_entry = DiaryEntry("Title","Contents")
    test_entry_2 = DiaryEntry("Title_2","Contents_2")
    test_entry_3 = DiaryEntry("Title_3","Contents_3")

    test_diary.add(test_entry)
    test_diary.add(test_entry_2)

    assert test_diary.all() == [test_entry,test_entry_2]

    test_diary.add(test_entry_3)

    assert test_diary.all() == [test_entry,test_entry_2,test_entry_3]


#test that count words returns the correct value with one entry

def test_count_words():
    test_diary = Diary()
    test_entry = DiaryEntry("Title","One Two Three Four")

    test_diary.add(test_entry)

    assert test_diary.count_words() == 4


#test that it returns the correct amount with multiple entries

def test_count_words_multiple():
    test_diary = Diary()
    test_entry = DiaryEntry("Title","One Two Three Four")
    test_entry_2 = DiaryEntry("Title","Five Six Seven Eight")

    test_diary.add(test_entry)
    test_diary.add(test_entry_2)

    assert test_diary.count_words() == 8


#test that it returns correft counts, even with poorly formatted entries

def test_count_words_format_errors():
    test_diary = Diary()
    test_entry = DiaryEntry("Title","    One Two 3     Four")
    test_entry_2 = DiaryEntry("Title","    5.0 Six:               Seven Eight 0.9   ")

    test_diary.add(test_entry)
    test_diary.add(test_entry_2)

    assert test_diary.count_words() == 9


#test that reading time returns the correct time in minutes 

def test_reading_time_accurate():
    test_diary = Diary()
    test_entry = DiaryEntry("Title", "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of  (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, , comes from a line in section 1.10.32.")

    test_diary.add(test_entry)

    assert test_diary.count_words() == 120
    assert test_diary.reading_time(20) == 6
    assert test_diary.reading_time(10) == 12



#test that reading time works with multipl entries

def test_reading_time_accurate_multiple():
    test_diary = Diary()
    test_entry = DiaryEntry("Title", "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of  (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, , comes from a line in section 1.10.32.")
    test_entry_2 = DiaryEntry("Title", "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of  (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, , comes from a line in section 1.10.32.")

    test_diary.add(test_entry)
    test_diary.add(test_entry_2)

    assert test_diary.count_words() == 240
    assert test_diary.reading_time(20) == 12
    assert test_diary.reading_time(10) == 24


#test that best entry function returns the closest out of three entries. the reader always has ones they can read fully

def test_best_entry_reading_time_all_possible():
    test_diary = Diary()

    test_entry = DiaryEntry("Test", "How are you?")                 #3 words
    test_entry_2 = DiaryEntry("Test", "How are you today?")         #4 words
    test_entry_3 = DiaryEntry("Test", "How are you doing today?")   #5 words

    test_diary.add(test_entry)
    test_diary.add(test_entry_2)
    test_diary.add(test_entry_3)

    #the following test has 1 wpm and 5 minutes, so should return entry 3, 5 words of it

    assert test_diary.find_best_entry_for_reading_time(1,5) == "How are you doing today?"

    #the following has 1 wpm and 3 minutes, so should return entry 1, all of it

    assert test_diary.find_best_entry_for_reading_time(1,3) == "How are you?"



#test that best entry function returns the closest, even when one doesnt match the exact number of words that can be read

def test_best_entry_reading_time_all_possible_no_matches():
    test_diary = Diary()

    test_entry = DiaryEntry("Test", "Whats up?")                    #2 words
    test_entry_2 = DiaryEntry("Test", "sup?")                       #1 words
    test_entry_3 = DiaryEntry("Test", "How are you?")               #3 words

    test_diary.add(test_entry)
    test_diary.add(test_entry_2)
    test_diary.add(test_entry_3)

    #the following test has 1wpm and 4 minutes - so 4 words. check to see if it returns test 3, even though it doesnt match exactly

    assert test_diary.find_best_entry_for_reading_time(1,4) == "How are you? How"

#test that best entry returns the closest, even amongst entries that are above and below. also checks cutoff function


def test_best_entry_reading_time_all_possible_above_below():
    test_diary = Diary()

    test_entry = DiaryEntry("Test", "Whats up?")                    #2 words
    test_entry_2 = DiaryEntry("Test", "sup?")                       #1 words
    test_entry_3 = DiaryEntry("Test", "How are you on this day?")               #6 words

    test_diary.add(test_entry)
    test_diary.add(test_entry_2)
    test_diary.add(test_entry_3)

    #the following test has 1wpm and 5 mins, should return the 6 lebgth one, but only first 5 words of it

    assert test_diary.find_best_entry_for_reading_time(1,5) == "How are you on this"


#tests if string is super short, then loops it

def test_best_entry_looping():
    test_diary = Diary()

    test_entry = DiaryEntry("Test", "Whats up? How are you today?")   

    test_diary.add(test_entry)

    assert test_diary.find_best_entry_for_reading_time(2,12) == "Whats up? How are you today? Whats up? How are you today? Whats up? How are you today? Whats up? How are you today?"


def test_final_mega_test():
    test_diary = Diary()

    test_entry = DiaryEntry("   Test", "")
    test_entry_2 = DiaryEntry("2.2", "Hello hello hello hello hello")
    test_entry_3 = DiaryEntry("","")
    test_entry_4 = DiaryEntry("This One", "The quick brown fox jumped over th lazy dog.")

    test_diary.add(test_entry)
    test_diary.add(test_entry_2)
    test_diary.add(test_entry_3)
    test_diary.add(test_entry_4)


    assert test_diary.all() == [test_entry,test_entry_2,test_entry_3,test_entry_4]
    assert test_diary.count_words() == 14
    assert test_diary.reading_time(2) == 7
    assert test_diary.find_best_entry_for_reading_time(7,2) == "The quick brown fox jumped over th lazy dog. The quick brown fox jumped"

