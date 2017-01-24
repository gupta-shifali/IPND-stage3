import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """initialize instance of class Movie and takes 5 inputs
        movie title, Storyline, Poster image link, Youtube railer link"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Displays the trailer of the movie"""
        webbrowser.open(self.trailer_youtube_url)
        
    
