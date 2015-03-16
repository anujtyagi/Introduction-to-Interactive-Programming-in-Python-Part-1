'''
Mini-project description — Rock-paper-scissors-lizard-Spock

Rock-paper-scissors is a hand game that is played by two people. The players count to three in unison and simultaneously "throw” one of three hand signals that correspond to rock, paper or scissors. The winner is determined by the rules:

Rock smashes scissors
Scissors cuts paper
Paper covers rock
Rock-paper-scissors is a surprisingly popular game that many people play seriously (see the Wikipedia article for details). Due to the fact that a tie happens around 1/3 of the time, several variants of Rock-Paper-Scissors exist that include more choices to make ties less likely.

Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of Rock-paper-scissors that allows five choices. Each choice wins against two other choices, loses against two other choices and ties against itself. Much of RPSLS's popularity is that it has been featured in 3 episodes of the TV series "The Big Bang Theory". The Wikipedia entry for RPSLS gives the complete description of the details of the game.

In our first mini-project, we will build a Python function rpsls(name) that takes as input the string name, which is one of "rock", "paper", "scissors", "lizard", or "Spock". The function then simulates playing a round of Rock-paper-scissors-lizard-Spock by generating its own random choice from these alternatives and then determining the winner using a simple rule that we will next describe.

While Rock-paper-scissor-lizard-Spock has a set of ten rules that logically determine who wins a round of RPSLS, coding up these rules would require a large number (5x5=25) of if/elif/else clauses in your mini-project code. A simpler method for determining the winner is to assign each of the five choices a number:

0 — rock
1 — Spock
2 — paper
3 — lizard
4 — scissors
In this expanded list, each choice wins against the preceding two choices and loses against the following two choices (if rock and scissors are thought of as being adjacent using modular arithmetic).

In all of the mini-projects for this class, we will provide a walk through of the steps involved in building your project to aid its development. A template for your mini-project is available here. Please work from this template.
'''
import random
def name_to_number(name):
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name =="lizard":
        return 3
    elif name =="scissors":
        return 4
    else :
        print "please enter rock/Spock/paper/lizard/scissors"

def number_to_name(number):
    if number==0:
        return "rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    elif number==4:
        return "scissors"    

def rpsls(player_choice): 
    print "\nPlayer chooses",player_choice
    player=name_to_number(player_choice)
    computerChoice=random.randrange(0,5)
    print "Computer chooses",number_to_name(computerChoice)
    if (player-computerChoice)%5==1 or (player-computerChoice)%5==2:
        print "Player wins!"
    elif(player-computerChoice)%5==3 or (player-computerChoice)%5==4:
        print "Computer wins!"
    else:
        print "Player and computer tie!"
        
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
