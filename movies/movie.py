import webbrowser


class Movie():
    """
    
    """

    def __init__(self, movie):
        self.poster = movie['poster']
        self.title = movie['title']
        self.trailer = movie['trailer']

    def show_trailer(self):
        webbrowser.open(self.trailer)