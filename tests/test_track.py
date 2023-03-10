from lib.track import Track

import pytest


"""

UNIT TESTS FOR TRACK CLASS

"""



#Tests to see if the Track class type saves title and artist variables

def test_saved_details():
    test_track = Track("Test Title","Test Artist")

    test_track.title == "Test Title"
    test_track.artist == "Test Artist"

#Tests to see if format returns the track name and artist in a good way

def test_track_format():
    test_track= Track("Test Title", "Test Artist")

    assert test_track.format() == "Test Title by Test Artist"

