
# Command definitions
c_new_game = "new"
c_continue = "resume"
c_help = "help"
c_exit = "exit"

execute = {
    c_new_game: f_new_game,
    c_continue: f_continue,
    c_help: f_help,
    c_exit: f_exit,
}

initial_prompt = "Enter a command ('{c_help}' for help): "
command = input(initial_prompt)

prompt = "||>" + " "

while command != c_exit:
    execute[command]()
    command = input(prompt)
