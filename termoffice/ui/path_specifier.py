# TODO - THIS IS JUST AN EXPERIMENT, VARIABLES NAMES AND READIBILITY NEED TO IMPROVE

from curses import (
    echo, newpad, curs_set
)
from .bases import Screen


class _PathSpecifier(Screen):

    def configuration(self):
        self.counter = 0
        # TODO - Replace newpad with subpad or newwin or derwin, newpad is overkilling here
        self.inputbox = newpad(3, 1000)

    def main(self):
        self.inputbox.refresh(0, 0, 0, 0, 3, 50)

        echo()
        all_chs = []
        x = ''

        while True:

            self.inputbox.border()
            # TODO - Make the keys such as backspaces usable, and prevent those keys to adding to the list
            self.inputbox.addstr(0, 1, "Enter something, typed letters cannot be reverted(yet):")
            self.inputbox.refresh(0, 0, 0, 0, 3, 100)
            self.inputbox.clear()

            all_chs.append(chr(self.inputbox.getch()))
            # TODO - Make the cursor follow the last typed letter
            printable_chs = all_chs[0:len(all_chs)]

            if len(all_chs) >= 100:
                del all_chs[0]

            for index, ch in enumerate(printable_chs):
                self.inputbox.addstr(0, 1, str(x))
                self.inputbox.addstr(1, 1+index, ch)


            # Used for debugging, should be removed once no longer need

            # self.screen.addstr(10, 10, str(len(printable_chs)))
            # self.screen.addstr(11, 10, str((len(printable_chs) >= 100)))
            # self.screen.addstr(12, 10, str(printable_chs[0])) 
            # self.screen.refresh()


PathSpecifier = _PathSpecifier()
