from lib.music_library import MusicLibrary
from lib.track import Track

import pytest


"""

INTEGRATION TESTS FOR MUSICLIBRARY AND TRACK CLASSES

"""

#test both classes available for testing in this suite

def test_test():
    test_lib = MusicLibrary()
    test_track = Track("Test Track", "Test Artist")

    assert test_lib.track_library == []
    assert test_track.title == "Test Track"
    assert test_track.artist == "Test Artist"


#Test when we add two tracks, we get them both back in the library list

def test_library_add():
    test_lib = MusicLibrary()
    test_track = Track("Test Track", "Test Artist")
    test_track2 = Track("Test Track2", "Test Artist2")

    test_lib.add(test_track)
    test_lib.add(test_track2)

    assert test_lib.track_library == [test_track,test_track2]

#Test when we try and add a non track type obj to music library, we get an error

def test_library_add_data_error():
    test_lib = MusicLibrary()
    test_track = [1,2,3]

    with pytest.raises(Exception) as e_info:
        test_lib.add(test_track)

    error_message = str(e_info.value)
    
    assert error_message == "Cannot add non-tracks to library!"


#Test when we add two tracks and search for the title, we get the track back

def test_search_by_title():
    test_lib = MusicLibrary()
    test_track = Track("Test Track", "Test Artist")
    test_track2 = Track("More Music!", "Test Artist2")

    test_lib.add(test_track)
    test_lib.add(test_track2)

    assert test_lib.search_by_title("More") == test_track2
    assert test_lib.search_by_title("Test") == test_track


#Test that when we search using only a small part of the word, we still get the track

def test_search_by_title_small():
    test_lib = MusicLibrary()
    test_track = Track("Test Track", "Test Artist")
    test_track2 = Track("More Music!", "Test Artist2")

    test_lib.add(test_track)
    test_lib.add(test_track2)

    assert test_lib.search_by_title("Mo") == test_track2
    assert test_lib.search_by_title("st") == test_track


#Test that if we search for a keyword not in any track names, we get a error message

def test_search_missing_song():

    test_lib = MusicLibrary()
    test_track = Track("Test Track", "Test Artist")
    test_track2 = Track("More Music!", "Test Artist2")

    test_lib.add(test_track)
    test_lib.add(test_track2)

    assert test_lib.search_by_title("GH") == "No track by that name"
