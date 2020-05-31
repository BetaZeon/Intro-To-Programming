import random
import time


def introDisplay():
    print("It feels like the end of the world as when you came to know ")
    time.sleep(2)
    print("about the Hanta Virus after the spread of Corona Virus."
          " A person named Elon Musk"
          " Found a way out ")
    time.sleep(2)
    print("of it but due to more population he can't take everyone to "
          "another planet named as Mars.")
    time.sleep(2)
    print("He than decided to set a game using which "
          "those who choose the right path will get chance"
          "to leave the planet with his spaceship.")
    print()


def pathChosen():
    path = ""
    while path != "1" and path != "2":   # Checking and Verifying the Input
        path = input("Which path will you choose? (1 or 2): ")
    return path


def pathCheck(pathChosen):
    print("You head down towards the spaceship")
    time.sleep(2)
    print("there's is a source of light that looks"
          " coming out of a person named CarryMinati"
          " who is familiar, that must be a good sign...")
    time.sleep(2)
    print("But you felt something different ....")
    print()
    time.sleep(2)
    correctPath = random.randint(1, 2)
    if pathChosen == str(correctPath):
        print("That was just the feeling of admiration"
              " from the brightness that person CarryMinati "
              "who started war against Tiktokers and saved us"
              " from getting exploited by those virus creaters"
              ".He also saved us "
              "from any type of infection and this showed that"
              " I successfully won the challenge to live.")
        print("Welcome home!")
    else:
        print("Here you meet with devil as you chose the path ")
        print("which will take you to such a disease "
              "which is ending this world")
        print("You now might get to know my name i.e. HANTA Virus.")


def begin_game():
    playAgain = "yes"
    while playAgain == "yes" or playAgain == "y":
        introDisplay()
        choice = pathChosen()
        pathCheck(choice)       # choice is equal to "1" or "2"
        playAgain = input("Do you want to play again?"
                          " (yes or y to continue playing): ")


begin_game()
