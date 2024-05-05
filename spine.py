import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()


class Context:
    def __init__(self, description, command_header, commands, elements, prompt):
        self.description = description
        self.command_header = command_header
        self.commands = commands
        self.commands['exit'] = exit
        self.prompt = prompt

    def command_body(self):
        phrases = self.commands.keys()
        return '\n'.join(phrases)

    def line(self):
        length = max(len(self.description), len(self.command_header)) + 2
        return length * '-'

    def __str__(self):
        # Fix this atrocity (later)
        return f"""
{self.line()}
{self.description}
        
{self.command_header}
{self.command_body()}
{self.line()}"""

    def request(self):
        return input('\n' + self.prompt + ' ')

    def execute(self, phrase):
        executor = self.commands[phrase]
        executor()

    def __call__(self):
        clear()
        print(self)
        self.execute(self.request())


# Context definitions
main_menu = Context('Welcome to our game.',
                    'Please peruse our humble selection of commands.',
                    {'new': lambda: new_game(), 'resume': lambda: resume()},
                    '>')

new_game = Context('You lie naked on soil. No light penetrates your closed eyelids. All is silent and still.',
                   "Consider.",
                   {'menu': lambda: main_menu()},
                   '>')

resume = Context('You have resumed',
                 'Nothing to see here.',
                 {'menu': lambda: main_menu()},
                 '>>')

# Run the game
main_menu()
