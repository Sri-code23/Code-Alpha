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

def display_hint(hint):
    for i in hint:
       print(i, end=" ")
    print()

def display_hangman(wrong_guesses):
    print(HANGMAN_PICS[wrong_guesses])

def main():
    answer=random.choice(words)
    print(answer)
    hint=["_"]*len(answer)
    wrong_guesses=0
    guesses=set()
    play=True

    while play:
        display_hangman(wrong_guesses)
        display_hint(hint)
        print()
        user_guess=input("Guess the letter: ").lower()
        while user_guess=="" or user_guess.isdigit() or len(user_guess)>1 or not user_guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            user_guess=input("Guess the letter: ").lower()
            guesses.add(user_guess)
            print(guesses)

        else: 
            if user_guess not in answer:
                print("Wrong guess ")
                guesses.add(user_guess)
                wrong_guesses+=1
                print(guesses)
            
            elif user_guess in answer:
                for i in range(len(answer)):
                    if answer[i]==user_guess:
                        hint[i]=user_guess
    
            if "_" not in hint:
                print(Fore.GREEN + "Congratulations! You've won!")
                play=False
                break
        if wrong_guesses==len(HANGMAN_PICS)-1:
            print(Fore.RED + "Sorry, you've lost!")
            print(HANGMAN_PICS[wrong_guesses])
            print("The correct word was: ", answer)
            play=False


if __name__=="__main__":
    main()