import random
import requests

user= input("What would you like to go by? ")

print(f"Hello {user}, let's play some hangman")

print("Guess a lower case letter! If you see a dash that is a space")


word = requests.get("https://random-word-api.herokuapp.com/word?key=TNOHO5HA&number=25")

chosen_word = random.choice(word.json())

guesses = ''

chances = 10


while chances > 0:         
    fail = 0             
    for char in chosen_word:      
        if char in guesses:    
            print(char)    
        elif char == "-":
            print("-")
        else:
            print("."),     
            fail += 1    
    if fail == 0:        
        print("You win!!")
        break              
    print('')
    guess = input("Guess a lowercase letter: ") 
    guesses += guess                    
    if guess not in word:  
        chances -= 1        
        print("Letter not in this word")    
        print(f"You have {chances} guesses") 
        if chances == 0:           
            print("You Lost!! :(")  