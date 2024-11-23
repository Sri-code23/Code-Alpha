import random

HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\ |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\ |
 /    |
      |
=========''', '''
  +---+
  |     ```` |
  O   |
 /|\\ |
 / \\ |
      |
=========
''']
def random_word():
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    random_wor=random.choice(words)
    return random_wor


def main():
    print("welcome to the game of hangman")
    print("-------------------------------")
    print("_ " * len(random_word()), sep="  ")

    guess=input("guess a word : ")
    while not guess=="":
        while guess.isdigit():
            print("invalid input")
        
    else:
        print("enter something ")        



if __name__ == "__main__":
    main()