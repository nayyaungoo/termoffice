from curses import initscr, endwin, curs_set, noecho
from abc import ABC, abstractmethod


class Screen(ABC):

    def start(self):
        self.screen = initscr()
        curs_set(0)
        noecho()
        self.maxy, self.maxx = self.screen.getmaxyx()

    @abstractmethod
    def main(self):
        ...

    def stop(self):
        endwin()

    def run(self):
        self.start()
        self.main()
        self.stop()

    def clear(self):
        self.screen.clear()
