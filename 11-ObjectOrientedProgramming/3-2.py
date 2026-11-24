###
# Class describing a piece of music
#

# class definition
class Song:
    # initial values are given when the object is created
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year

    # Returns the song data as a string (4 lines)
    def __str__(self):
        # \n starts a new line inside one string
        return (f'Performer: {self.artist}\n'
                f'Title:     {self.title}\n'
                f'Album:     {self.album}\n'
                f'Year:      {self.year}')

# object creation
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

## object usage - print() calls __str__ automatically
print(song1)
print()
print(song2)