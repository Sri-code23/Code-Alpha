import random
from colorama import Fore,Style

HANGMAN_PICS = [
  '''
  ┌───┐
  │   │
      │
      │
      │
      │
┌─────┴──┐
└────────┘''', 
'''
  ┌───┐
  │   │
  O   │
      │
      │
      │
┌─────┴──┐
└────────┘''',
'''
  ┌───┐
  │   │
  O   │
  │   │
      │
      │
┌─────┴──┐
└────────┘''',
'''
  ┌───┐
  │   │
  O   │
 /│   │
      │
      │
┌─────┴──┐
└────────┘''',
'''
  ┌───┐
  │   │
  O   │
 /│\\  │
      │
      │
┌─────┴──┐
└────────┘''',
 '''
  ┌───┐
  │   │
  O   │
 /│\\  │
 /    │
      │
┌─────┴──┐
└────────┘''',
 '''
  ┌───┐
  │   │
  O   │
 /│\\  │
 / \\  │
      │
┌─────┴──┐
└────────┘''']

words = ['car', 'bag', 'tree', 'apple', 'pen', 'book', 'chair', 'table', 'phone', 'computer']


def display_hangman(wrong_guess):
    if wrong_guess==6:
        print("──────────────────────────" )
        print(Fore.BLACK + HANGMAN_PICS[wrong_guess] + Style.RESET_ALL)
        print("──────────────────────────" ) 
    else:   
        print() 
        print("──────────────────────────" )
        print(Fore.GREEN + HANGMAN_PICS[wrong_guess] + Style.RESET_ALL)
        print("──────────────────────────" )
    #"┌", "┐", "─", "│", "┘ " , "└", "┼", "┬", "┴"", "┼", "┌", "┐", "┬", "┴", "├", "┤", "┼"

def display_hint(hint):
    for i in hint:
        print(i, end=" ")
    print()

def main():
    print("──────────────────────────────────────────────────────────────" )
    print("Welcome to Hangman Game!")
    print("Guess the word by guessing letters. You have 7 wrong guesses.")
    print("──────────────────────────────────────────────────────────────" )
    print()
    correct_answer=random.choice(words)
    hint=["_"]*len(correct_answer)
    wrong_guesses=0
    okay_to_play=True
    guesses=set()

    while okay_to_play:
        display_hangman(wrong_guesses)
        display_hint(hint)
        print()
        guess=input ("Guess a letter: ").lower()
        while guess=="" or guess.isdigit() or len(guess)>1:
            if guess=="":
                print(Fore.LIGHTRED_EX + "Atleast enter something"+ Style.RESET_ALL)
                guess=input ("Guess a letter: ").lower()
            elif guess.isdigit():
                print(Fore.LIGHTRED_EX + "Enter a letter not a number" + Style.RESET_ALL)
                guess=input ("Guess a letter: ").lower()
            elif len(guess)>1:
                print(Fore.LIGHTRED_EX + "Enter one letter at a time" + Style.RESET_ALL)
                guess=input ("Guess a letter: ").lower()
        else:
            if guess not in correct_answer:
                wrong_guesses+=1
                guesses.add(guess)
                print(Fore.LIGHTRED_EX + f"Wrong guess!" + Style.RESET_ALL)

            elif guess in correct_answer:
                if guess in guesses:
                    print(Fore.LIGHTRED_EX + "you have already guessed this.."+ Style.RESET_ALL)
                else:
                    guesses.add(guess)
                    for i in range(len(correct_answer)):
                        if correct_answer[i]==guess:
                            hint[i]=guess
                            display_hint(hint)
            
            if wrong_guesses==len(HANGMAN_PICS)-1:
                print(Fore.LIGHTRED_EX + f"Game Over! The correct answer was {correct_answer}")
                print(Fore.LIGHTRED_EX + HANGMAN_PICS[wrong_guesses] + Style.RESET_ALL)
                print(Fore.LIGHTRED_EX + f"wrong guesses: {wrong_guesses}" + Style.RESET_ALL)
                okay_to_play=False
                play_again=input(Fore.LIGHTBLUE_EX + "do you want to play again (yes/no): ").lower()
                while not play_again=="no":
                    if play_again=="":
                        print("Atleast enter something")
                        play_again=input(Fore.LIGHTBLUE_EX + "do you want to play again (yes/no): ").lower()
                    
                    elif play_again=="yes":
                            main()
                    else:
                        print("invalid input")
                        play_again=input(Fore.LIGHTBLUE_EX + "do you want to play again (yes/no): "+ Style.RESET_ALL).lower()      

                else:
                    print(Fore.LIGHTYELLOW_EX +"Thanks for playing" + Style.RESET_ALL)
                    okay_to_play=False

if __name__ == "__main__":
    main()


