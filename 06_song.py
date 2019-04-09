"""
15 min

A playlist is considered a repeating playlist if any of the songs contain
a reference to a previous song in the playlist. Otherwise, the playlist will end
with the last song which points to None.

Implement a function is_repeating_playlist that, efficiently with respect to
time used, returns true if a playlist is repeating or false if it is not.

For example, the following code prints "True" as both songs point to each other.

    first = Song("Hello")
    second = Song("Eye of the tiger")

    first.next_song(second);
    second.next_song(first);

    print(first.is_repeating_playlist())




    class Song:
        def __init__(self, name):
            self.name = name
            self.next = None

        def next_song(self, song):
            self.next = song

        def is_repeating_playlist(self):
            return None

    first = Song("Hello")
    second = Song("Eye of the tiger")

    first.next_song(second);
    second.next_song(first);

    print(first.is_repeating_playlist())
"""


class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        playlist = {self}
        song = self.next
        while song:
            if song in playlist:
                return True
            else:
                playlist.add(song)
                song = song.next
        return False


first = Song("Hello")
second = Song("Eye of the tiger")

first.next_song(second)
second.next_song(first)

print(first.is_repeating_playlist())
