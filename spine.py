import os


class Context:
    def __init__(self, description, command_intro, prompt):
        self.description = description
        self.command_intro = command_intro
        self.commands = {'exit': exit}
        self.prompt = prompt

    def set_commands(self, commands):
        self.commands.clear()
        self.commands.update(commands)
        self.commands['exit'] = exit

    def command_list(self):
        phrases = self.commands.keys()
        return '\n'.join(phrases)

    def __str__(self):
        return self.description + 2 * '\n' + self.command_intro + '\n' + self.command_list()

    def request(self):
        return input('\n' + self.prompt + ' ')

    def execute(self, phrase):
        executor = self.commands[phrase]
        executor()

    def __call__(self):
        os.system('cls' or 'clear')
        print(self)
        self.execute(self.request())


# Main menu context
mm_description = 'Welcome to the Main Menu context.'
mm_command_intro = 'Enter one of the following commands.'
mm_prompt_string = '>'
main_menu = Context(mm_description, mm_command_intro, mm_prompt_string)

# New game context
ng_description = 'You have entered the New Game context.'
ng_command_intro = "Return to the menu when you're ready."
ng_prompt_string = '|>'
new_game = Context(ng_description, ng_command_intro, ng_prompt_string)

# Resume context
r_description = 'You have resumed.'
r_command_intro = 'Nothing to see here.'
r_prompt_string = '->>'
resume = Context(r_description, r_command_intro, r_prompt_string)

# Command lists:
main_menu.set_commands({'new': new_game, 'resume': resume})
new_game.set_commands({'menu': main_menu})
resume.set_commands({'menu': main_menu})

# Run the game
main_menu()
