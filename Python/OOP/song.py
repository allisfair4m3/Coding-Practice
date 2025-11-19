class Song:

    def __init__(self, name, artist, year, genre):
        self.name = name
        self.artist = artist
        self.year = year
        self.genre = genre
    
    def Play(self):
        print(f"We're now playing a song called {self.name}")
    
    def Stop(self):
        print(f"The last song we played was {self.name}")

    def Info(self):
        print(f"The song currently playing is {self.name} which was performed by {self.artist} in the year of {self.year} that belongs to {self.genre} genre")