def main():
    print('Игра Быки и Коровы, приветствует тебя!')
    while(True):
        print("\nСыграем?")
        print("1 А то ж!")
        print("2 Пффф, игры для детей!")
        flag=input()
        if (flag=='1'): 
            playGame()
        elif (flag=='2'): 
            sys.exit()
        else: print("Моя твоя не понимай :(")
#####
def playGame():
    myDigits=[]
    myDigits=makeDigits()
    print('Ну что, готов прочитать мои мысли?\nКакие четыре цифры я загадала?')
    while (True):
        yourNumber=input()
        yourDigits=list(yourNumber)        
        if (checkDigits(yourDigits)):
            cow,bull=exploreDigits(myDigits,yourDigits)
            print('Итак, сколько же в нашем стаде коров? А быков?\n',cow,'и',bull)
            if (bull==4):
                print('Вах, какой маладэц!')
                break
            else:
                print('М-да, сразу ясно, что ты не телепат. Давай ещё раз!')
#####
def makeDigits():
    import random
    random.seed()
    digits=list('0123456789')
    random.shuffle(digits)
    digits=digits[0:4]
    print(digits)    
    return digits
#####
def checkDigits(digits):
    if ((len(digits)!=4)|(len(set(digits))!=4)|(len(set(digits+list('0123456789')))!=10)):
        print('Эй, ты чего? Я же сказала ЧЕТЫРЕ ЦИФРЫ, и они все РАЗНЫЕ')
        return False
    else:
        return True
#####
def exploreDigits(myDigits,yourDigits):
    cow=len(myDigits+yourDigits)-len(set(myDigits+yourDigits))
    bull=0
    for i in range(4):
        if (myDigits[i]==yourDigits[i]):
            bull=bull+1
    return(cow,bull)
#####
import sys
main()