from curses import initscr, endwin, curs_set, noecho


class Screen(object):

    def configuration(self):
        ...

    def start(self):
        self.screen = initscr()
        self.configuration()
        curs_set(0)
        noecho()

    def stop(self):
        endwin()

    def run(self):
        self.start()
        self.main()
        self.stop()

    def clear(self):
        self.screen.clear()
