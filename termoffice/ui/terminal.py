from curses import echo, newwin
from .bases import Screen


class _Terminal(Screen):

    def configuration(self):
        self.console = newwin(self.maxy-3, self.maxx-1, 0, 1)
        self.cinput = newwin(3, self.maxx-1, self.maxy - 3, 1)
        echo()

    def main(self):

        while True:
            self.cinput.border()
            self.console.border()

            self.cinput.refresh()
            self.console.refresh()

            self.cinput.addstr(1, 2, "> ")
            command = self.cinput.getstr(1, 4)
            
            self.cinput.clear()
            self.console.addstr(1, 1, command)

            self.cinput.refresh()
            self.console.refresh()

Terminal = _Terminal()

if __name__ == '__main__':

    Terminal.run()
    print(Terminal)
    print(Terminal.maxy)
