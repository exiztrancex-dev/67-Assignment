import random

def choose_word ():
    word_list = ["APPLE","IVORY","HOUSE","JUICE","BEACH","EAGLE" ]
    computer_word = random.choice(word_list)
    return computer_word


def get_guess (previous_guesses): 
    
    valid_guess = False
    
    while valid_guess == False:
        try: 
         player_guess = str(input("Guess a word! (Please enter a 5 letter word)")).upper()
         
         if (len(player_guess)) != 5:
                raise Exception

         if player_guess in previous_guesses:
             print("Already guessed that. Try again!")
             continue
         
         valid_guess = True
         previous_guesses.append(player_guess)
          
            
        
        except:
            print("Not a valid input! Please enter a 5 letter word")
            player_guess = str(input("Guess a word! (Please enter a 5 letter word"))

     
    return player_guess 



def evaluate_guess(computer_word, player_guess):

    feedback = ""
    
    for i in range(len(player_guess)):
        
        if player_guess[i] == computer_word[i]:
            feedback += "G"

        elif player_guess[i] in computer_word and player_guess[i] != computer_word[i]:
            feedback += "Y"
        else:
            feedback += "-"

    return feedback


def display_guess(player_guess, feedback, guess_counter):
    spaced_guess = " ".join(player_guess).upper()
    spaced_feedback = " ".join(feedback).upper()
    
    print(f"Attempt {guess_counter} of 6")
    
    print(f"Guess: {player_guess}")
    print(f"Feedback: {feedback}")


def has_won(computer_word, player_guess):
    
    
    if computer_word == player_guess:
        has_won = True
    else:
        has_won = False

    return has_won
        
        