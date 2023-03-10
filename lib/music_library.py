from lib.track import Track

class MusicLibrary:
    # Public properties:
    #   tracks: a list of strings representing tracks

    def __init__(self):
        self.track_library = [] #creates an empty list

    def add(self, track):

        try:                    #attempts to access the tracks title - if it doesnt exist, raises an error
            if type(track.title) == str:
                self.track_library.append(track)

        except:
            raise Exception("Cannot add non-tracks to library!")

        
    
    def search_by_title(self, keyword):

        track = None

        for i in self.track_library:
            name = i.title
            if keyword in name:
                track = i

        if track == None:
            return "No track by that name"
        else:
            return track


