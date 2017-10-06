import urllib2
import sys


class Movie():
    def __init__(self, title, poster_url, trailer_url):
        # Names of instance variable is defined in fresh_tomatoes.py
        self.title = title
        # Verify the poster_url as a valid target
        try:
            urllib2.urlopen(poster_url)
            self.poster_image_url = poster_url
        except urllib2.HTTPError:
            print """Poster URL is not valid.
                Please check and restart the program"""
            sys.exit()
        # It is hard to verify the youtube video link so
        # I skip the verification in trailer_url
        self.trailer_youtube_url = trailer_url
