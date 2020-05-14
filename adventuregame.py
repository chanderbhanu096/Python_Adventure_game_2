import random
import time


def displayIntro():
    print("I am not good at english and script so i just madethis game up I"
          "hope you enjoy \n")
    time.sleep(1)
    print("Enough Intro about me Let's get started with the the game intro"
          "\n")
    time.sleep(2)
    print("you will Be given Three random out of which you will select \n")
    time.sleep(3)
    print("Whether you will join the Jungle party or you'll be eaten By Wild"
          " animals All depends On your Luck \n")
    time.sleep(3)
    print("One time you may enter the jungle party or second time you maybe "
          "eaten by Wild animals .It all depends on you \n")
    time.sleep(3)
    print("Even Me who created this game can't be sure by selcting which"
          " particaular option I will win the game Becasue everything is"
          " random \n")
    time.sleep(3)


def choosePath():
    path = ""
    while path != "1" and path != "2" and path != "3":
        path = input("Which path will you choose? (1 / 2 / 3): ").strip()
    return path


def checkPath(chosenPath):
    print("You head down the path \n")
    time.sleep(2)
    print("there's a lake arby that looks familiar, that must be a good "
          "sign... \n")
    time.sleep(2)
    print("But you are also having goosebumps \n")
    time.sleep(2)
    item = []
    correctPath = random.choice(["1", "2", "3"])
    if chosenPath == str(correctPath):
        print("Those goosebumps was the feelign of visiting familiar place, "
              "which looks amazing at midnight which you visit daily on day "
              "time \n")
        time.sleep(2)
        print("Welcome to Night party and for winning the game \n")
        time.sleep(2)
    else:
        print(" Well you were too positive . Those were not goosebumps, those "
              "were chills because of Wild animals Roar \n")
        time.sleep(2)
        print("Sorry, but you are eaten by Not Wild Animals but vampire , you "
              "heart has been snapped out \n")
        time.sleep(2)
        print("You died a miserable death \n")


def playAgain():
    userinput = input("Do you want to play again? (yes to continue "
                      "playing / no to quit): ").strip().lower()
    if userinput == "yes":
        print("game is restarting")
        playgame()
    elif userinput == "no":
        print("bye game is exiting now")
    else:
        playAgain()


def playgame():

    displayIntro()
    choice = choosePath()
    checkPath(choice)
    playAgain()

playgame()
