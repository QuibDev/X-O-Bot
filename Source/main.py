# create an X-O-BOT

# rule 1. you can only fill in one box at a time.
# rule 2. you can only fill empty boxes.

# How to win

# if you get three boxes in a row (vertical, horizontal, diagonal)
# you win


# now i have a grid now what?

# when player removes something the place should be removed with an O
# when bot removes something the place should be removed with an X

# at 14:13,
# the game works mostly, but the bots command won't update on grid
# if the player commands are updated and vice versa


from typing import Tuple


def main():

    print("!!! WELCOME TO XO BOT !!!")

    promt = str(input("Do you want to play the game? (Y/N): "))

    if promt.lower() == "y":

        import random
        import time

        y_gridSize = 3
        x_gridSize = 3

        grid = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
        ]

        playerTurn, botTurn = True, False

        botMark = "O"
        playerMark = "X"

        while True:

            # render playing grid
            time.sleep(0.5)
            print('\n')
            for columns in range(y_gridSize):
                print(grid[columns])

            # Player move -->

            if playerTurn:

                playerMove = eval(input("\nEnter your move (x,y): ", ))

                print("\nPLAYER CHOSE: {}".format(playerMove))

            elif botTurn:

                # bot move -->

                # an arbitiary wait for the bot

                print("\nBot's turn")
                time.sleep(1.0)
                print("thinking...")
                time.sleep(random.uniform(1.0, 2.0))

                botMoveList = []

                try:

                    for columns in range(y_gridSize):
                        botMove = random.choice(grid[columns])
                        if botMove != botMark and botMove != playerMark:
                            botMoveList.append(botMove)

                    botMove = random.choice(botMoveList)
                    print('Bot Choosed {}'.format(botMove))

                except IndexError:
                    print("Bot is out of options!")
                    time.sleep(0.5)
                    print("Bot will pass")

            # !--- Update the moves on the grid

            if playerTurn:
                try:
                    for columns in range(y_gridSize):
                        if playerMove in grid[columns] and playerMove != botMark and playerMove != playerMark:
                            grid[columns][grid[columns].index(
                                playerMove)] = playerMark
                            #print("Removed item at index {}".format(k))
                except ValueError:
                    print("That move is unavailable! Please try again")
                    continue  # it should restart the loop not the game

            elif botTurn:

                for columns in range(y_gridSize):
                    if botMove in grid[columns]:
                        grid[columns][grid[columns].index(
                            botMove)] = botMark
                        #print("Removed item at index {}".format(k))

            # Reset the turns -->

            if playerTurn:
                playerTurn, botTurn = False, True
            elif botTurn:
                playerTurn, botTurn = True, False

    else:
        print("THANKS FOR PLAYING!")

    return


main()
