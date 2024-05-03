import os


class Context:
    def __init__(self, description, command_header, commands, prompt):
        self.description = description
        self.command_intro = command_header
        self.commands = commands
        self.commands['exit'] = exit
        self.prompt = prompt

    def set_commands(self, commands):
        self.commands.clear()
        self.commands.update(commands)
        self.commands['exit'] = exit

    def __str__(self):
        return f"""
        {self.description}
        
        {self.command_intro}
        {self.command_list()}
        """

    def request(self):
        return input('\n' + self.prompt + ' ')

    def execute(self, phrase):
        executor = self.commands[phrase]
        executor()

    def __call__(self):
        os.system('cls || clear')
        print(self)
        self.execute(self.request())


# Context definitions
main_menu = Context('Welcome to the Main Menu context.',
                    'Enter one of the following commands.',
                    {'new': lambda: new_game(), 'resume': lambda: resume()},
                    '>')

new_game = Context('You have entered the New Game context.',
                   "Return to the menu when you're ready",
                   {'menu': lambda: main_menu()},
                   '|>')

resume = Context('You have resumed',
                 'Nothing to see here.',
                 {'menu': lambda: main_menu()},
                 '->>')

# Run the game
main_menu()
