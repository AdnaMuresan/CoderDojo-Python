from random import randrange

#functie noua care citeste
#de la tastatura

def citesteTastatura(mesaj):
    myNumber = (int)(input(mesaj))
    return myNumber

def guessNumber(range):
    computerNumber = randrange(range)
    myNumber = citesteTastatura("Ghici: ")

    while(computerNumber != myNumber):
        myNumber = citesteTastatura("Ghici: ")

    if(computerNumber == myNumber):
        print("Correct guess")


guessNumber(10)
