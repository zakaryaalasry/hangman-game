import random
print("Welcome to Hangman game....\nThere will be a hidden word\nYou have to find out the word by guessing the letter each time")
print("You have 6 attempts to guess the word")
words = [
    "apple", "banana", "cherry", "orange", "grape", "peach", "mango", "lemon",
    "watermelon", "strawberry", "blueberry", "raspberry", "pineapple", "kiwi",
    "papaya", "pear", "plum", "apricot", "fig", "date", "coconut", "avocado",
    "tomato", "carrot", "potato", "onion", "garlic", "pepper", "pumpkin",
    "broccoli", "spinach", "lettuce", "cabbage", "cucumber", "radish",
    "zucchini", "eggplant", "beans", "peas", "corn", "ginger", "celery",
    "beetroot", "turnip", "squash", "artichoke", "asparagus", "cauliflower",
    "leek", "okra" ]
hangman_ascii = [
    """
     _______
    |/      
    |       
    |       
    |       
    |       
   _|___
    """,
    """
     _______
    |/      |
    |       
    |       
    |       
    |       
   _|___
    """,
    """
     _______
    |/      |
    |      (_)
    |       
    |       
    |       
   _|___
    """,
    """
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |       
   _|___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |       
   _|___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / \\
   _|___
    """
]


the_word = random.choice(words)
length = len(the_word)
planks = []
for i in range(length):
  planks.append("-")
print("Your word is:-")
print("".join(planks))
# the_letter = input("Please guess a letter: ")
the_guessed_letters = []
attempt = 0
max_attempt = 6
while attempt < max_attempt:
    the_letter = input("Please guess a letter: ").lower()
    if the_letter in the_guessed_letters:
        print("You've already guessed this letter")
        continue
    the_guessed_letters.append(the_letter)
    let_length = len(the_letter)
    if not the_letter.isalpha and let_length != 1:
        print("You should enter a letter")
    else:
        if the_letter not in the_word:
            print("wrong guess")
            print("".join(planks))
            if attempt != 4:
                print(f"You have {5-attempt} tries left")
            else:
                print(f"You have {5-attempt} try left")
            print(hangman_ascii[attempt])
            attempt += 1
            continue
        else:
            for i in range(length):
                if the_letter == the_word[i]:
                    planks[i] = the_letter
            print("".join(planks))
        if "".join(planks) == the_word:
            break
        
if "".join(planks) == the_word:
    print("\nCongratulations 👏🎉🎉! You guessed the word.\n\n")
else:
    print("\n☠️ Game Over ☠️! The word was:", the_word ,"\n\n")
