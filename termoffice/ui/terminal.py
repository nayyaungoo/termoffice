from curses import echo, newwin
from .bases import Screen


class _Terminal(Screen):

    def configuration(self):

        self.console = newwin(
            self.maxy-3,    # Maximum y minus 3
            self.maxx-1,    # Maximum x minus 1
            0, 
            1
        )

        self.cinput = newwin(
            3,
            self.maxx-1,    # Maximum x minus 1
            self.maxy - 3,  # y before 3 of Maximum y
            1
        )

        echo()
        self.acceptable_commands = {
            'clear'
        }

    def main(self):

        while True:
            self.cinput.border()
            self.console.border()

            self.cinput.refresh()
            self.console.refresh()

            received_command = self.get_command()

            self.cinput.clear()
            self.validate_command(received_command)

            self.cinput.refresh()
            self.console.refresh()

    def validate_command(self, command):
        if command not in self.acceptable_commands:
            self.console.addstr(1, 1, f"console: {command} is not a command.")
            self.console.addstr(2, 1, f"Use --help to display all the usable commands >w<.")

    def get_command(self) -> str:
        self.cinput.border()
        self.cinput.refresh()
        self.cinput.addstr(1, 2, "> ")
        return self.cinput.getstr(1, 4).decode('utf-8')

Terminal = _Terminal()

if __name__ == '__main__':

    Terminal.run()
    print(Terminal)
    print(Terminal.maxy)
