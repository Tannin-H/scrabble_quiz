import random
import string
import pickle


list_of_lists = []
my_file = open("words", "r")
for line in my_file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_of_lists.append(line_list)
my_file.close()

def check_int(txt):
    while True:
        try:
            num = int(input(txt))
            return num
        except ValueError:
            print("please enter an integer")


def check_y_or_n(answer):
    while answer != "y" and answer != "yes" and answer != "n" and answer != "no":
        answer = input(answer)
    return answer



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


def scrabble_cheater():
    print()
    print("Welcome to the scrabble word finder this  will generate all of the possible words from your letters"
          "you have provided and display them from largest to smallest")
    input_char = input("Please enter all of the available characters ").lower().strip()
    asset = list(input_char)
    print(asset)
    gen_words = find_words(asset)
    print("all of the possible solutions are")
    gen_words.sort(key=len)
    for word in gen_words:
        print(word)
    gen_more = check_y_or_n("would you like to generate more words [y]es or [n]o? ")
    if gen_more == "y":
        scrabble_cheater()
    else:
        main()


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
    print("Only the correct spelling will be accepted")
    print("There are no 1 letter words")
    print("Each letter can only be used once and each word used once")
    print("Finally your score is determined by the accumulation of the lengths of words you spell")
    print()
    total, correct = guessing(rand_letters, answers)
    print("{} {}".format("your total score was", total))
    print("The other possible combinations are")
    answers.sort(key=len)
    for word in answers:
        print("{} {} {}".format("score", len(word), word))
    play_again = check_y_or_n("would you like to play again [y]yes or [n]no ")
    if play_again == "y":
        print()
        quiz_main()
    else:
        print()
        main()


def guessing(rand_letters, answers):
    corr_total = 0
    corr_list = []
    guessed = []
    correct = False
    guess = input("please press enter to begin guessing ")
    while guess != "f":
        print()
        print("{} {}".format("the letters you have available to use are ", rand_letters))
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
        if not correct:
            print("sorry that guess was incorrect please try again")
        correct = False
        print("{} {}".format("the words you have previously guessed are", guessed))
    print()
    return corr_total, corr_list


def main():
    print()
    print("welcome to the online word guesser quiz")
    print("you will be given random letters from the alphabet and the goal is to see how many combinations of words "
          "you are able "
          "make")
    print("if you would like to take part in the quiz press [1]")
    print("if you would like to use the scrabble cheater press [2]")
    print("If you would like to exit please press 3")
    choice = check_int("please enter [1, [2] or [3] ")
    while choice != 1 or choice != 2:
        if choice == 1:
            quiz_main()
        elif choice == 2:
            scrabble_cheater()
        elif choice == 3:
            exit()
        else:
            choice = check_int("please enter [1 or [2] ")


main()
