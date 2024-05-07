from collections import namedtuple
from math import ceil
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


Style = namedtuple('Style', ['corner', 'h_bord', 'v_bord', 'prompt'])
default_style = Style('+', '-', '|', '>')


class Entity:
    def __init__(self, description, commands, style=default_style):
        self.description = description
        self.commands = commands
        self.commands['Exit the game.'] = exit
        self.corner = style.corner
        self.h_bord = style.h_bord
        self.v_bord = style.v_bord
        self.prompt = style.prompt

    def promptize(self, command):
        return self.prompt + ' ' + command

    def lines(self):
        description_lines = self.description.split('\n')
        option_lines = [self.promptize(command) for command in self.commands]
        return description_lines + option_lines

    def width(self):
        longest_length = max(len(line) for line in self.lines())
        min_width = longest_length + 2

        def next_multiple_above(n, t):
            return ceil(t / n) * n

        return next_multiple_above(len(self.h_bord), min_width)

    def border_line(self):
        # Construct border_line
        thickness = len(self.v_bord)
        corner_slice = thickness * self.corner
        border_line = str(corner_slice + self.h_bord * (self.width() // len(self.h_bord)) + corner_slice)
        return ((thickness + 1) // 2) * (border_line + '\n')

    def marginalize(self, string):
        l_margin = self.v_bord + ' '
        r_margin = ' ' + self.v_bord

        return f"{l_margin}{string.ljust(self.width() - 2)}{r_margin}"

    def __str__(self):
        description_lines = [self.marginalize(line) for line in self.description.split('\n')]
        description = '\n'.join(description_lines)

        marginalized_commands = [self.marginalize(self.prompt + ' ' + command) for command in self.commands]
        command_lines = '\n'.join(marginalized_commands)

        return f"{self.border_line()}{description}\n{self.border_line()}{command_lines}\n{self.border_line()}"

    def request(self):
        num_spaces = len(self.v_bord) + 1
        full_prompt = num_spaces * ' ' + self.prompt + ' '
        return input(full_prompt)

    def __call__(self):
        def execute(phrase):
            matches = [command for command in self.commands if phrase.lower() in command.lower()]

            if len(matches) == 0:
                print(f'\n"{phrase}" doesn\'t match any commands.')
                execute(self.request())
            elif len(matches) == 1:
                selected = matches[0]
                executor = self.commands[selected]
                executor()
            else:
                print(f'\n"{phrase}" matches {len(matches)} commands.')
                execute(self.request())

        clear()
        print(self)
        execute(self.request())


class Item(Entity):
    def __init__(self, access_command, description, commands, style=default_style):
        super().__init__(description, commands, style)
        self.access_command = access_command


class Place(Entity):
    def __init__(self, description, commands, contents, style=default_style):
        super().__init__(description, commands, style)
        self.contents = contents

    def lines(self):
        lines = [self.promptize(content.access_command) for content in self.contents]
        return super().lines() + lines

    def __str__(self):
        marginalized_contents = [self.marginalize(line) for line in self.lines()]
        content_body = '\n'.join(marginalized_contents)

        return super().__str__() + content_body + self.border_line()


class Container(Item, Place):
    def __init__(self, access_command, description, commands, contents, style=default_style):
        Item.__init__(access_command, description, commands, style)
        Place.__init__(description, commands, contents, style)


# Context definitions
main_menu = Entity('Welcome to our game.',
                   {'Start a new game.': lambda: new_game(),
                    'Continue a previous game.': lambda: resume()})

new_game = Entity('You lie naked on soil.\nNo light penetrates your closed eyelids.\nAll is silent and still.',
                  {'Return to the main menu.': lambda: main_menu()})

resume = Entity('You have resumed.',
                {'Return to the main menu.': lambda: main_menu()})

# State variables:
stack = [main_menu]

# Run the game
while len(stack) > 0:
    context = stack.pop(-1)
    context()
