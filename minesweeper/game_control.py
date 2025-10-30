import webbrowser
from minesweeper import *

class GameControl:

    def __init__(self, url):
        self.url = url

    def open_url_in_browser(self):
        webbrowser.open(self.url)



channel = GameControl('minesweeper.html')
channel.open_url_in_browser()
