import random
import string

list_of_lists = []
my_file = open("words", "r")
for line in my_file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_of_lists.append(line_list)

my_file.close()


def find_words(char):
    print(char)
    for item in list_of_lists:
        for letter in item[0]:
            if letter == char[0]:
                print(item)


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
    return characters


def quiz_main():
    print()
    print("Thank you for choosing to partake in the quiz the rules are as follows")
    rand_letters = gen_letters()
    print("{} {}".format("the letters you have available to use are ", rand_letters))
    total, correct = guessing(rand_letters)
    print("{} {}".format("your total score was", total))
    play_again = input("would you like to play again [y]yes or [n]no ")
    if play_again == "y":
        quiz_main()


def guessing(rand_letters):
    corr_total = 0
    corr_list = []
    guessed = []
    guess = input("please press enter to begin guessing ")
    while guess != "f":
        print()
        print(rand_letters)
        guess = input(
            "please enter you guess and press enter or if you are finished guessing press [f] ").lower().strip()
        guessed.append(guess)
        for item in list_of_lists:
            if guess == item[0] and guess != "f":
                letters = list(guess)
                find_words(letters)
                corr_total += len(item[0])
                corr_list.append(item)
                print("congratulations that was correct ")
                print("{} {} ".format("The total amount of points you have is", corr_total))
        print("{} {}".format("the words you previously guessed were", guessed))
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
