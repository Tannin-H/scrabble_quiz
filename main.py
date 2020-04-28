import random
import string
import pickle
from itertools import permutations

list_of_lists = []
my_file = open("words", "r")
for line in my_file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_of_lists.append(line_list)
my_file.close()


def find_words(char):
    possibles = []
    used = []
    check = 0
    for item in list_of_lists:
        for letter in item[0]:
            if letter in used:
                check = 0
            if letter in char:
                check += 1
                used.append(letter)
        if check == len(item[0]):
            possibles.append(item[0])
            check = 0
            used.clear()

        used.clear()
        check = 0
    return possibles
    print(possibles)


def scrabble_cheater():
    asset = []
    num_char = int(input("please enter how many letters you have available to use "))
    for num in range(0, num_char):
        input_char = input("please enter one of the characters you have available to use ")
        asset.append(input_char)
    find_words(asset)


def gen_letters():
    letters_string = string.ascii_lowercase
    letters = list(letters_string)
    characters = random.choices(letters,
                                weights=[2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1,
                                         1, 1], k=10)
    if "a" not in characters and "e" not in characters and "i" not in characters and "o" not in characters and "u" not in characters:
        characters.remove(characters[0])
        characters.append("a")
        print("added")
    return characters


def quiz_main():
    rand_letters = gen_letters()
    answers = find_words(rand_letters)
    print(answers)
    print()
    print("Thank you for choosing to partake in the quiz the rules are as follows")
    print("{} {}".format("the letters you have available to use are ", rand_letters))
    total, correct = guessing(rand_letters, answers)
    print("{} {}".format("your total score was", total))
    play_again = input("would you like to play again [y]yes or [n]no ")
    if play_again == "y":
        quiz_main()


def guessing(rand_letters, answers):
    corr_total = 0
    corr_list = []
    guessed = []
    correct = False
    guess = input("please press enter to begin guessing ")
    while guess != "f":
        print()
        print(rand_letters)
        guess = input(
            "please enter you guess and press enter or if you are finished guessing press [f] ").lower().strip()
        guessed.append(guess)
        for item in answers:
            if guess == item and guess != "f":
                answers.remove(item)
                corr_total += len(item)
                corr_list.append(item)
                print("congratulations that was correct ")
                print("{} {} ".format("The total amount of points you have is", corr_total))
                correct = True
        if correct == False:
            print("sorry that guess was incorrect please try again")
        correct = False
        print("{} {}".format("the words you have previously guessed are", guessed))
    print()
    return corr_total, corr_list


def main():
    print("welcome to the online word guesser")
    print("you will be given random letters from the alphabet and the goal is to see how many combinations of words "
          "you are able "
          "make")

    print("if you would like to take part in the quiz press [1]")
    print("if you would like to use the scrabble cheater press [2]")
    choice = int(input("please enter [1 or [2] "))
    if choice == 1:
        quiz_main()
    elif choice == 2:
        print("CHEATER")


main()
