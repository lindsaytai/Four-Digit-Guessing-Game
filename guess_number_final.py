#copyright lindsay cheng 2021

import time
import os
import random

play = True
guess_counter = 0
results = []

#makes random number
grab_four_digits = random.sample(range(0,9), k = 4)

spin1 = str(grab_four_digits[0])
spin2 = str(grab_four_digits[1])
spin3 = str(grab_four_digits[2])
spin4 = str(grab_four_digits[3])
random_number = str(spin1) + str(spin2) + str(spin3) + str(spin4)

#start game
os.system("cls")
print("\n\n\n")
print("Hello! I am thinking of a passcode with four numbers.")
print("* = number is in correct location.")
time.sleep(2)
print("0 = number is in passcode but not in correct location.")
time.sleep(2)
print("Type \"help\" for a list of possible commands.")
time.sleep(2)
print("Make sure your guess is four digits, with no repeating numbers!")
time.sleep(2)

while play == True:

    guess_counter = guess_counter + 1

    guess = input("\nMake a guess: ")        
               
    if guess == "help":
        
        print("Type \"hint\" for a hint.")
        time.sleep(2)
        print("Type \"tell\" if you want to know the answer.")
        time.sleep(2)
        print("Type \"quit\" anytime to exit game.")
        time.sleep(2)
        print("For teacher mode (to briefly show the answer), type \"teacher mode\"")
              
    elif guess == "hint":
        print("One number is...", random.choice(random_number))

    elif guess == "quit":
        print("Okay, see you next time!")
        break

    elif guess == "teacher mode":
        print(random_number)
        time.sleep(5)
        os.system("cls")
        
    elif guess == "tell":
        print("The answer is...", random_number)
        
        play_again = input("Play again? y/n: ")

        if play_again == "y":                     
            guess_counter = 0
            grab_four_digits = random.sample(range(0,9), k = 4)
            
            spin1 = str(grab_four_digits[0])
            spin2 = str(grab_four_digits[1])
            spin3 = str(grab_four_digits[2])
            spin4 = str(grab_four_digits[3])
            random_number = str(spin1) + str(spin2) + str(spin3) + str(spin4)     

            os.system("cls")
            print("\n\n\n")
            print("Hello! I am thinking of a passcode with four numbers.")

        else:
            print("Thank you for playing! See you next time!")
            break
        
    elif guess not in ["hint", "quit", "tell", "help", "teacher mode"]:
        is_int = guess.isdigit()
        
        if is_int == False:
            print("Invalid input. Please enter integers!")
            results = []
            
        else:
            pass
                  
        digit_count = len(guess)
       
        if digit_count != 4:
            print("Please type a four-digit number!")
            print("By the way, the answer was", random_number)
            time.sleep(2)
            results = []
            break

        #checks if passcode is in correct place
        if guess[0] == spin1:
            results.append("*")                 
            
        if guess[1] == spin2:
            results.append("*")      
            
        if guess[2] == spin3:
            results.append("*")

        if guess[3] == spin4:
            results.append("*")
            
        #checks if number IS in passcode but in wrong place
        if guess[0] != spin1 and guess[0] in [spin2, spin3, spin4]:
            results.append("0")

        if guess[1] != spin2 and guess[1] in [spin1, spin3, spin4]:
            results.append("0")
                
        if guess[2] != spin3 and guess[2] in [spin1, spin2, spin4]:
            results.append("0")            

        if guess[3] != spin4 and guess[3] in [spin1, spin2, spin3]:
            results.append("0")            

        if len(guess) != len(set(guess)):
            print("No repeating digits!")
            results = []
            
    print(str(guess_counter) + ". Results:", results)
    results = []
    
    if guess == random_number:
        print("You win! Guess correct!")       
   
        play_again = input("Play again? y/n: ")

        if play_again == "y":                     
            
            grab_four_digits = random.sample(range(0,9), k = 4)
            
            spin1 = str(grab_four_digits[0])
            spin2 = str(grab_four_digits[1])
            spin3 = str(grab_four_digits[2])
            spin4 = str(grab_four_digits[3])
            random_number = str(spin1) + str(spin2) + str(spin3) + str(spin4)   
            guess_counter = 0
            
            os.system("cls")
            print("\n\n\n")
            print("Hello! I am thinking of a passcode with four numbers.")

        else:
            print("Thank you for playing! See you next time!")
            break
