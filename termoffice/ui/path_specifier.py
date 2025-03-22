# TODO - THIS IS JUST AN EXPERIMENT, VARIABLES NAMES AND READIBILITY NEED TO IMPROVE
# This is basically last in first out

from curses import (
    echo, newpad, curs_set, 
    KEY_BACKSPACE, KEY_LEFT, KEY_RIGHT
)
from curses.ascii import isprint
from .bases import Screen
from itertools import chain


class _PathSpecifier(Screen):

    def configuration(self):
        self.counter = 0
        # Updated TODO: Tried replacing with a derwin, doesn't seem to work, either should come
        # up antoher one or solve why it doesn't work 
        self.inputbox = newpad(3, 100)

    def main(self):

        echo()
        all_chs = []
        x = 0
        y = 0
        curs_set(1)
        edit_mode = False

        # Characters like ':', Control Keys, Backspaces etc..(This variable is just in case created)
        restricted_chs = list(chain.from_iterable([list(range(0, 32)), [58, 42, 63, 34, 60, 62, 124, 126, 127]]))

        self.inputbox.box()
        self.inputbox.addstr(0, 1, "Enter something, typed letters cannot be deleted(yet):")
        self.inputbox.refresh(0, 0, 0, 0, 3, 100)

        o = 0

        while True:

            # Updated TODO - Backspace is completed, other keys usability need to implement

            # Receive a letter from user and append them into the lists
            self.inputbox.keypad(True)
            received_ch = self.inputbox.getch()

            if received_ch not in (KEY_LEFT, KEY_RIGHT) and not edit_mode:

                # if received_ch not in restricted_chs:
                if isprint(received_ch) and received_ch not in restricted_chs:

                    all_chs.append(chr(received_ch))

                    # TODO - Make the cursor follow the last typed letter

                    # Left out the first inputted characters to give some space 
                    # for last inputted letter when the list reaches its capacity
                    # of 98 letters(100 - border widths which is 2)

                    if len(all_chs) >= 98:
                        # Will raise error if only delete at 100 chs because the
                        # max it goes is 98, and once it reaches 98, left out the
                        # the first inputted chs, to do so, we need a counter
                        x += 1

                    self.inputbox.clear()

                # The backspace
                elif received_ch == KEY_BACKSPACE:
                    del all_chs[-1]
                    self.inputbox.clear()

                printable_chs = all_chs[0+x:len(all_chs)]

                editable_chs = printable_chs[0:len(printable_chs)]

                # Need to call it again, i mean this is not a refactored code so..
                self.inputbox.border()
                self.inputbox.addstr(0, 1, "Enter something, typed letters cannot be deleted(yet):")
                self.inputbox.refresh(0, 0, 0, 0, 3, 100)

                for index, ch in enumerate(printable_chs):
                    self.inputbox.addstr(1, 1+index, ch)
                    

            else:
                for index, ch in enumerate(printable_chs):
                    self.inputbox.addstr(1, 1+index, ch)

                # The left and right keys
                if received_ch == KEY_LEFT:
                    editable_chs.pop(-1)
                    y += 1

                if received_ch == KEY_RIGHT:
                    editable_chs.append(printable_chs[len(editable_chs)])
                    y += 1

                for index, ch in enumerate(editable_chs):
                    self.inputbox.addstr(1, 1+index, ch)

                if self.inputbox.getyx()[1] == len(printable_chs)+1:
                    edit_mode = False

                else:
                    edit_mode = True


                self.screen.addstr(20, 1, str(all_chs))
                self.screen.addstr(24, 1, str(self.inputbox.getyx()))
                self.screen.addstr(25, 1, str(len(printable_chs)+1))
                self.screen.addstr(26, 1, str(edit_mode))
                self.screen.refresh()


            if received_ch not in (KEY_LEFT, KEY_RIGHT) and edit_mode == True:
                self.screen.addstr(22, 1, str(chr(received_ch)))
                if isprint(received_ch) and received_ch not in restricted_chs:
                    all_chs.insert(self.inputbox.getyx()[1], chr(received_ch))
                self.screen.refresh()

                printable_chs2 = all_chs[0+x:self.inputbox.getyx()[1]]
                lefts = all_chs[self.inputbox.getyx()[1]:len(all_chs)]

                # Need to call it again, i mean this is not a refactored code so..
                self.inputbox.border()
                self.inputbox.addstr(0, 1, "Enter something, typed letters cannot be deleted(yet):")
                self.inputbox.refresh(0, 0, 0, 0, 3, 100)

                for index, ch in enumerate(printable_chs2):
                    self.inputbox.addstr(1, 1+index, ch)

                self.inputbox.addstr(1, self.inputbox.getyx()[1]+o, chr(received_ch))
                o += 1

                for index, ch in enumerate(lefts):
                    self.inputbox.addstr(1, self.inputbox.getyx()[1], ch)
                self.screen.addstr(10, 1, str(lefts))
                self.screen.refresh()


            self.inputbox.refresh(0, 0, 0, 0, 3, 100)

            # debugging addstrs can be wrtten here down below
            # =========================================================
            # self.screen.addstr(10, 10, str(len(printable_chs)))
            # self.screen.addstr(11, 10, str((len(printable_chs) >= 100)))
            # self.screen.addstr(12, 10, str(printable_chs[0]))
            # self.screen.addstr(19, 0, f"      Len of all_ch: {len(all_chs)}")
            # self.screen.addstr(20, 0, f"Len of printable ch: {len(printable_chs)}")

            # y = 92 # \
            # y = 47 # /
            # self.screen.addstr(22, 0, f"ASCII {y} = {repr(chr(y))}")

            # self.screen.addstr(24, 0, f"Current Inpuuted Ch: {received_ch}")

            # self.screen.refresh()


PathSpecifier = _PathSpecifier()
