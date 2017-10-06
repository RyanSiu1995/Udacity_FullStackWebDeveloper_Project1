from fresh_tomatoes import open_movies_page
import media

if __name__ == "__main__":
    # Initialize the target movies
    listOfMovies = [media.Movie(
            "Shutter Island",
            "https://upload.wikimedia.org/wikipedia/en/thumb/7/76/Shutterislandposter.jpg/220px-Shutterislandposter.jpg",  # NOQA
            "https://www.youtube.com/watch?v=5iaYLCiq5RM"  # NOQA
        ),
        media.Movie(
            "Life is beautiful",
            "https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/Vitaebella.jpg/220px-Vitaebella.jpg",  # NOQA
            "https://www.youtube.com/watch?v=pAYEQP8gx3w"  # NOQA
        ),
        media.Movie(
            "Interstellar",
            "https://www.wired.com/wp-content/uploads/2014/09/Interstellar_ALT_Artowrk-660x1030.jpeg",  # NOQA
            "https://www.youtube.com/watch?v=zSWdZVtXT7E"  # NOQA
        ),
        media.Movie(
            "SAO Ordinal Scale",
            "https://d3ieicw58ybon5.cloudfront.net/full/u/114b3bd30a4842bf89b65cd05261e0ff.jpg",  # NOQA
            "https://www.youtube.com/watch?v=VNxxReVeVDI"  # NOQA
        ),
        media.Movie(
            "The Battleship Island",
            "https://upload.wikimedia.org/wikipedia/en/thumb/4/4a/Battleship_Island_Poster.jpg/220px-Battleship_Island_Poster.jpg",  # NOQA
            "https://www.youtube.com/watch?v=GmA2YIWRF0M"  # NOQA
        )]
    # Invoke the function given
    open_movies_page(listOfMovies)
