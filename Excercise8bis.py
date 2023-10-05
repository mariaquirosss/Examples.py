##Dice simulator: Write a program that simulates the roll of two dice and calculates the sum of
##the values obtained.

import random

def roll_two_dice():
    die1= random.randint(1,6)
    die2= random.randint(1,6) 
    return die1, die2

def main(): 
 
    die1, die2 = roll_two_dice()
    print (f"El primer dado tiene de resultado", die1)
    print(f"El segundo dado tiene de resultado", die2)
    print(f"La suma total es: ",die1+die2)

def main():
    result=[] #Lista para almacenar los resultados de los datos    
    num_exec = 1000

    for i in range (1,1001): #repetir 1000 veces
        die1, die2 = roll_two_dice()
        total= die1 + die2
        result.append((i, die1, die2, total))

if __name__ == "__main__":
    main()
