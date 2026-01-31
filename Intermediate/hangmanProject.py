import random

stages = ['''
+----+
|    |
     |
     |
     |
=========
''','''
+----+
|    |
O    |
     |
     |
=========
''','''
+----+
 |    |
 O    |
/    |
     |
=========
''','''
+----+
 |    |
 O    |
/ \  |
     |
=========
''','''
+----+
 |    |
 O    |
/ \  |
|    |
=========
''','''
+----+
 |    |
 O    |
/ \  |
| |  |
=========
''']
words = ["komal", "tarak", "dhoni", "apple", "akash", "nandu"]
word = random.choice(words)

display = ["_"] * len(word)
used_letters = []
lives = len(stages) - 1

print("WELCOME TO THE HANGMAN GAME")
print(f"Word has {len(word)} letters")
print(" ".join(display))
print(f"You have {lives} lives\n")

while lives > 0 and "_" in display:
    guess = input("Guess a letter: ").lower()

    if guess in used_letters:
        print("You already guessed that letter")
        continue

    used_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct!")
    else:
        print("Wrong guess!")
        print(stages[len(stages)-1-lives])
        lives -= 1
        print(f"Lives remaining: {lives}")

    print("Word:", " ".join(display))
    print("Guessed letters:", used_letters)
    print("-" * 30)

if "_" not in display:
    print("CONGRATULATIONS! YOU WON ")
else:
    print("...GAME OVER...")
    print("The word was:", word)
