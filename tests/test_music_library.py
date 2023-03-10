from lib.music_library import MusicLibrary
from lib.track import Track

import pytest



'''

UNIT TESTS FOR MUSICLIBRARY CLASS


'''


#Check that whenm a library object is made, it has an empty list within

def test_library_exists():
    test_library = MusicLibrary()

    assert test_library.track_library == []


