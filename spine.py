import os


class Context:
    def __init__(self, description, command_intro, commands, prompt):
        self.description = description
        self.command_intro = command_intro
        self.commands = commands
        self.commands['exit'] = exit
        self.prompt = prompt


    def command_list(self):
        phrases = self.commands.keys()
        return 'Enter a command.\n' + '\n'.join(phrases)

    def __str__(self):
        return self.description + 2*'\n' + self.command_intro + '\n' + self.command_list()

    def request(self):
        return input('\n' + self.prompt + ' ')
    
    def execute(self, phrase):
        executor = self.commands[phrase]
        executor()

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self)
        while True:
            self.execute(self.request())


# Command definitions
def new_game():
    print('Yep this is the game.')

def resume():
    print('Resuming :)')

mm_description = "Welcome to our game."
mm_command_intro = "Enter one of the following commands."
mm_commands = {'new': new_game, 'resume': resume}
mm_prompt_string = '>'

main_menu = Context(mm_description, mm_command_intro, mm_commands, mm_prompt_string)

main_menu()