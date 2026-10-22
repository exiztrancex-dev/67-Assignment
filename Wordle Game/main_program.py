from worlde_functions import choose_word, get_guess, evaluate_guess, display_guess, has_won

def play_wordle():
    playing = True
    
    while playing:
        # Welcome message 
        print("Welcome to Wordle!")
        print("Guess the five-letter word.\n")
        print("G = correct letter and position")
        print("Y = correct letter, wrong position")
        print("- = letter is not in the word\n")
        
        secret_word = choose_word()
        previous_guesses = []
        guess_counter = 1
        won_game = False
        
        # Giving the user 6 tries
        while guess_counter <= 6:
            # Get a valid 5-letter, un-guessed word
            player_guess = get_guess(previous_guesses)
            
            # Evaluate the guess
            feedback = evaluate_guess(secret_word, player_guess)
            
            # Displaying the guess, feedback, and the attempt #
            display_guess(player_guess, feedback, guess_counter)
            
            # Check if they won
            if has_won(secret_word, player_guess):
                print("Congratulations! You solved the puzzle.")
                won_game = True
                break
                
            guess_counter += 1
            
        # If they run out of attempts, reveal the word
        if not won_game:
            print(f"You lost The word was: {secret_word}")
            
        # Ask to play again and looping
        play_again = input("Would you like to play again? ").strip().lower()
        if play_again != "yes" and play_again != "y":
            print("Thanks for playing!")
            break

#starting the actual game
play_wordle()
