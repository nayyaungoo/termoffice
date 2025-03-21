# TODO - THIS IS JUST AN EXPERIMENT, VARIABLES NAMES AND READIBILITY NEED TO IMPROVE
# This is basically last in first out

from curses import (
    echo, newpad
)
from .bases import Screen


class _PathSpecifier(Screen):

    def configuration(self):
        self.counter = 0
        # Update: Tried replacing with a derwin, doesn't seem to work, either should come
        # up antoher one or solve why it doesn't work 
        self.inputbox = newpad(3, 100)

    def main(self):

        echo()
        all_chs = []
        x = ''
        self.inputbox.border()
        # TODO - Make the keys such as backspaces usable, and prevent those keys to adding to the list
        self.inputbox.addstr(0, 1, "Enter something, typed letters cannot be deleted(yet):")
        self.inputbox.refresh(0, 0, 0, 0, 3, 100)

        while True:

            # Receive a letter from user and append them into the lists
            all_chs.append(chr(self.inputbox.getch()))
            # TODO - Make the cursor follow the last typed letter
            printable_chs = all_chs[0:len(all_chs)]

            # Delete the very first inputted character to give some space 
            # for next inputted letter when the list reaches its capacity
            # of 98 letters(100 - border widths)

            if len(all_chs) >= 98:
                # Will raise error if only delete at 100 chs because the
                # max it goes is 98, and once it reaches 98, immediately
                # remove the first inputted ch
                del all_chs[0]

            for index, ch in enumerate(printable_chs):
                self.inputbox.addstr(0, 1, str(x))
                self.inputbox.addstr(1, 1+index, ch)

            self.inputbox.refresh(0, 0, 0, 0, 3, 100)

            # Used for debugging, should be removed once no longer need
            # =========================================================
            # self.screen.addstr(10, 10, str(len(printable_chs)))
            # self.screen.addstr(11, 10, str((len(printable_chs) >= 100)))
            # self.screen.addstr(12, 10, str(printable_chs[0])) 
            # self.screen.refresh()


PathSpecifier = _PathSpecifier()
