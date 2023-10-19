def greet_player():
    player = input("what is your player name?")
    if player is None:
        raise Exception("you need to enter a name")
    return "Ready for battle {}?".format(player)