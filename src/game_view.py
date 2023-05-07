from view.blackjack_form import BlackjackForm

#players = ["Marco", "Pri", "Duda", "Manu", "Jessica", "Eni", "Guara", "Maico"]
players = ["Marco", "Pri", "Duda", "Manu", "Jessica"]
from view.blackjack_form import BlackjackForm
form = BlackjackForm(players)
form.start_game()
form.run_game()

