import random
import string

list_of_lists = []
my_file = open("words", "r")
for line in my_file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_of_lists.append(line_list)

my_file.close()

"""def find_words(num_char):
    potentials = []
    char = []
    for list in list_of_lists:
        if len(list[0]) <= num_char:
            potentials.append(list)

    for item in potentials:
        for letter in len(item[0]):
            if letter == char[0] and letter == char[1] and letter == char[3]:
                print(item)


def scrabble_cheater():
    num_char = int(input("please enter how many letters you have available to use "))

    for num in range(0, num_char):
        input_char = input("please enter one of the characters you have available to use ")
        char.append(input_char)
    find_words()"""


def gen_letters():
    letters_string = string.ascii_lowercase
    letters = list(letters_string)
    charecters = random.choices(letters,
                                weights=[5, 1, 1, 1, 5, 1, 1, 1, 5, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 5, 1, 1, 1,
                                         1, 1], k=5)
    return charecters


def quiz_main():
    print()
    print("Thankyou for choosing to partake in the quiz the rules are as follows")
    gen_letters()
    rand_letters = gen_letters()
    print("{} {}".format("the letters you have available to use are ", rand_letters))
    guessing(rand_letters)


def guessing(rand_letters):
    corr_total = 0
    corr_list = []
    guess = input("please press enter to begin guessing ")
    while guess != "f":
        print()
        print(rand_letters)
        guess = input(
            "please enter you guess and press enter or if you are finished guessing press [f] ").lower().strip()
        for item in list_of_lists:
            if guess == item[0]:
                corr_total += 1
                corr_list.append(item)
                print(corr_total)
    quiz_main()

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


main()
