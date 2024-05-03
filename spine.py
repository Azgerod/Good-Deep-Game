
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

prompt = "|>" + " "

while command != c_exit:
    execute[command]()
    command = input(prompt)
    
    





# make the story. we need a good story, gotta make it compelling or at least make it compelling to learn the lore
#build the outline
#gotta build the main quest / everything around it.




"""
You see a dead guy on the side of the road. what 
Talk (you enter speech mode)
Attack (you choose an attack)
Use item (you may choose an item within your inventory)
Cancel / Ignore (you ignore the current matter, and break out of the loop)


I think a good way to handle com






OUTLINE:
* Story
* Main menu
* First room
* the prompt changes. for example, level 1 has >>>, level 2 has --->, level 3 has -->>, other combinations. The formulais non-linear, but if you decide to re-arrange the layers such that you see the linear pattern, you unlock a code or hidden message. You look at the order of the layers, and take that order to mean something else, and you go deeper into the schitzo memes
* How many layers?
* How big are layers?
* How much time per room?
* What's the "bonfire" mechanic?
* How much detail per room?
* Dream stuff / simulation explanation (Deep in the lore)
* Themes of layers
* Big bad (chaos source ma?)
* Apophenia
* Adversarial relationship to players (confirmation bias them into traps etc, subversion of expectation)
* Illusions, different node connections
* Dungeon changing over time, losing maps
* Alchemy type thing
* List of deceptions
* Semi-living levels with personalities (flesh walls)
* Mimic level (set them up to think it's looping, then subvert all knowledge to murder them)
* Schizophrenia game
* FIght over the course of a layer
* Enemy that adapts to you and learns your behaviours etc
* Endless corridors
* Pits
* Spacial fuckery
* Temporal fuckery ()
* Random respawn points, weighted inversely by depth
* Layer(s) above the surface ()
* Capitalize on ALL FEARS
* Always reward schizo thoughts ("nah, that's schizo")
* Patterns in things
* Have text make shapes
* Capitalization
* Everything has multiple meanings
* Many sources talking shit about this one innocent guy trying to make you kill them
* UI starts betraying you
* a place full of fragile pottery and you hear voices telling you to break it
* weird things to do with mirrors, water, and reflections. seeing things in the reflections that aren't there
* You go camping, and there's a creature that puts out your campfire and talks to you in the darkness. toys with you
* Liminal spaces. we've got to take that and play with backrooms things





MAIN MENU: Different every time, possibly dependent on in-game memes
* New Game
* Continue
* Help (one of the commands leads to credits, recursive "help" command changes, leading them deviously into information hazard/reward)
* Exit













"""