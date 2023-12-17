class Song:
    
    # Class Attribute
    count = 0
    genres = []
    genre_count = {}
    artists = []
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        print("Adding song to count")
        cls.count += 1

    
    @classmethod
    def add_to_genres(cls, genre):
        print(f"Adding genre: {genre}")
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # To avoid repetition
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Example usage
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")        
thriller = Song("Thriller", "Michael Jackson", "Pop")
another_song = Song("Another Song", "Artist", "Pop")

# Accessing attributes
print(ninety_nine_problems.name)
print(ninety_nine_problems.artist)
print(ninety_nine_problems.genre)

print(Song.count)    
print(Song.genres)  

# Accessing genre_count
print(Song.genre_count)

# Accessing artist_count
print(Song.artist_count)