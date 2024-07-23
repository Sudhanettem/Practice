import random

print("Hello Sudha Welcome to Game")

def choice():
    options = ["rock" , "paper","scissors"]
    player_choice = input(f"please enter your option {options} :")
    computer_choice = random.choice(options)
    choices = {"player" : player_choice , "computer": computer_choice }
    return choices

def Game(player , computer):

    if(player == computer):
        return "It's a tie"
    
    if (player == "rock"):
        if(computer == "paper") :
            return "you lose !! paper covers rock"
        else :
            return "You Win !!! Rock smashes scissors"
    elif (player == "paper"):
        if(computer == "scissors"):
            return "You loose !!! scissors cut paper"
        else:
            return "You win !!!! Paper covers rock"
    else:
        if(computer == "rock"):
            return "You loose !! rock smashes scissors"
        else:
            return "You win !!! scissors cut paper"
        
choices = choice()
print(f"you choose {choices["player"]}, computer choose {choices["computer"]}")
print(Game(choices["player"] , choices["computer"]))
        
list = ["Hrudhvick" ,"Yashrika" , "Ravi","Sudha"]
list.sort()
print(f"{list}Nettem family")


def test ():
    resp = "Hello function...."
    return resp

print(test())


# play= input("please enter any number :: ")
# if(play % 2 == 1):
#     print("Even number")
# else:
#     print("odd number")