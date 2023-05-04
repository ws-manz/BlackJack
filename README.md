# Blackjack Game
A simple implementation of the classic Blackjack card game in Python.

## Installation
Clone or download the repository.
Install the required packages by running pip install -r requirements.txt.
Usage
To start the game, simply run python main.py from the command line. The game will prompt you to enter the number of players, their names, and their initial bankroll. Once the game is started, follow the on-screen instructions to play.

## Rules
The goal of Blackjack is to beat the dealer by having a hand value greater than the dealer's hand value without going over 21. The value of a hand is the sum of the point values of the individual cards. Face cards (kings, queens, and jacks) are worth 10 points, aces are worth 1 or 11 points (whichever is more advantageous to the player), and all other cards are worth their numerical value.

At the start of each round, players are dealt two cards face up, and the dealer is dealt two cards (one face up and one face down). Players can choose to "hit" (receive additional cards) or "stand" (keep their current hand) in an effort to get as close to 21 as possible without going over. If a player's hand value exceeds 21, they "bust" and lose the round. Once all players have had a turn, the dealer reveals their face-down card and hits until their hand value is 17 or greater.

## Features
Supports multiple players with customizable names and bankrolls.
Implements standard Blackjack rules, including splitting pairs and insurance bets.
Graphical user interface with card graphics and sound effects.
Detailed game statistics, including win/loss records and highest bankroll.
Save and load game state functionality.

## Credits
This project was inspired by the following resources:

* Blackjack Rules and Strategy
* Card images
* Card shuffling algorithm
