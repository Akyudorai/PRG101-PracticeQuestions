# HARDMODE SCENARIO!!
# You're building digital version of the Blackjack card game
# Write a program with defined functions that allow you to complete at least 1 whole round of Blackjack.

# RULES OF THE GAME
# A deck of 52 cards is shuffled before 2 cards are drawn from the deck and given to the player.
# Each card has a value, ranging from 1 to 10, with each face card having a maximum value of 10, 
# and Ace cards having an optional value of 1 or 11.
# If the sum of the players cards exceeds 21, the player loses the game
# Otherwise, they have the option of choosing an option to "Hit" or "Stand"
# HIT: the player is given another card from the deck, adding to their total value, 
#      and proceeds to check the win condition again, as well as HIT or STAND if necessary
# STAND: The player ends their turn accepting their total current value

# Once the player turn has ended, the dealer would get a turn, following the same rules, trying get a better score,
# or match the players score.

# TODO 1: Create functions that allow you to:
    # - Shuffle the deck with a full set of playing 52 cards, considering face cards as a value of 10
    # - Draw a card from the deck, removing it from the deck
    # - Calculate the score of a particular hand, whether that be the players or the dealers
    # - Any others you think you might need

# TODO 2: Initialize any variables you need to be persistent / global across this game

# TODO 3: Draw two cards and add them to the players hand to begin the game.

# TODO 4: Start a while loop to manage our game.  As long as the player has not lost, the loop will persist

    # TODO 5: Calculate the score for the players hand and show them what cards they have

    # TODO 6: If they can continue to play, then ask them if they want to HIT or STAND

        # TODO 7: If the player chooses HIT, draw a card and repeat the loop
                # Otherwise, end the loop and print the score.


# TODO BONUS: Repeat the same steps as above, but automate the process so the dealer gets a hand and will try to 
            # Match the players score or beat it.

