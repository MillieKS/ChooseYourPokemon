# ChooseYourPokemon/game/game.py
# from api.api import random_pokemon


class TopTrumps():
    def __init__(self):
        self.player1 = []
        self.computer = []
        self.player1_deck_size = 20
        self.computer_deck_size = 20
        self.rounds_of_play = 10

    # def get_random_pokemon(self):
    #     return api.random_pokemon()


    def greet_player(self):
        max_retries = 5  # Set the maximum number of retries
        for i in range(max_retries):
            if i < max_retries:
                player = input("What is your player name?")
                if len(player) == 0:
                    print("You need to enter a name.")
                else:
                    ready = input(f"Ready for battle, {player}?").lower()
                    if ready == "yes":
                        print("Let's go!")
                        return  # Exit the method if the user is ready. 
                                # Return doesn't continue to ask the readiness question after the user has indicated readiness
                    else:
                        print("Not ready. Let's ask again.")
        else:
            print("Maximum number of retries reached. Exiting.")
    
    
    def game(self):
        pass



    

 
