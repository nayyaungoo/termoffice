from curses import (
    A_REVERSE, A_DIM,
    KEY_UP, KEY_DOWN,
)
from .bases import Screen


class _MainMenu(Screen):
    menu = (
        " Leave Termoffice :<  ",
        " Create new project   ",
        " Load a saved project ",
        " Save current project ",
        " Project Settings     ",
    )

    selected_item = 0
    project_loaded = True

    def main(self):
        self.draw_menu()

    def draw_menu(self, menu=menu):

        while True:

            for index, item in enumerate(menu):
                if self.selected_item == index:
                    self.screen.addstr(1+index, 2, f"{index}.{item}", A_REVERSE)
                elif not self.project_loaded and index in (2, 3):
                    self.screen.addstr(1+index, 2, f"{index}.{item}", A_DIM)
                else:
                    self.screen.addstr(1+index, 2, f"{index}.{item}")

            self.screen.keypad(True)

            key = self.screen.getch()

            if key == KEY_UP and self.selected_item > 0:
                self.selected_item -= 1

                if not self.project_loaded and self.selected_item in (2, 3):
                    self.selected_item = 1

            elif key == KEY_DOWN and self.selected_item < len(menu) - 1:
                self.selected_item += 1

                if not self.project_loaded and self.selected_item in (2, 3):
                    self.selected_item = 4

            # 48: 0
            elif key == 48:
                self.selected_item = 0

            # 49: 1
            elif key == 49:
                self.selected_item = 1

            # 50: 2
            elif key == 50:
                self.selected_item = 2

            # 51: 3
            elif key == 51:
                self.selected_item = 3

            # 52: 4
            elif key == 52:
                self.selected_item = 4

            # 10: Enter
            if key in (10, 48, 49, 50, 51, 52):
                break

MainMenu = _MainMenu()
