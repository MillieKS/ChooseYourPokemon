import api.api

class TopTrumps():
    def __init__(self):
        self.player1 = []
        self.computer = []
        self.player1_deck_size = 20
        self.computer_deck_size = 20
        self.rounds_of_play = 10

    def random_pokemon(self):
        return api.random_pokemon()

    def game():
        pass


    def greet_player():
        player = input("what is your player name?")
        if player is None:
            raise Exception("you need to enter a name")
        return "Ready for battle {}?".format(player)