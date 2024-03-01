import random as r
# TODO 1 Making A list Filled with all the possible Words
Hangman_Ascii = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
    '''
]
WORD_LIST = ["giraffe", "elephant", "lion"]
MISTAKES_PERMITTED = 0
word_choice_array = []
correct = False

# TODO 2 Grab a one of the word from the list
game = True
while game:
    word_choice = r.choice(WORD_LIST)
    # the word choice is made into an array
    word_array = list(word_choice)
    print(word_array)
    print(f" The Answer is: {word_choice}")

    # TODO 3 Make an Array with all the blank letters of the word
    for i in range(0, len(word_array)):
        word_choice_array.append("_ ")

    # TODO 4 User Choice

    while word_choice_array != word_array:

        # Print The Blanks or Not
        for i in range(len(word_choice_array)):
            print(word_choice_array[i], end = "")

        choice = input("\nWhat is the possible letter?\n")

        for i in range(len(word_choice_array)):
            if choice == word_choice[i]:
                word_choice_array[i] = choice
                correct=True

        # TODO 5 Count The Hangman

        if correct:
            correct = False
        else:
            if MISTAKES_PERMITTED == 6:
                game = False
                break
            print("Wrong Letter: \n " + Hangman_Ascii[MISTAKES_PERMITTED])
            MISTAKES_PERMITTED = MISTAKES_PERMITTED + 1


    play_again = input("Do you want to play again? Y|N").lower()
    if play_again == "n":
        game = False
    else:
        MISTAKES_PERMITTED = 0
        word_choice_array = []
        correct = False





