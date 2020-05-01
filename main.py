import random
import string
import pickle

"""opens the file containing words as a list and assigns it to a variable"""
pickle_in = open("words_list", "rb")
list_of_lists = pickle.load(pickle_in)

pickle_in.close()


def check_int(txt):
    """Takes in the parameter txt which displays the question and then validates the user input using try except"""
    while True:
        try:
            num = int(input(txt))
            return num
        except ValueError:
            print("please enter an integer")


def check_y_or_n(answer):
    """Uses the parameter answer to determine if the user input is yes, y, no or n"""
    while answer != "y" and answer != "yes" and answer != "n" and answer != "no":
        answer = input(answer).strip().lower()
    return answer


def find_words(char):
    """function used to generate all of the possible words from the given players given letters(char)
    and return them as a list(possibles)"""
    possibles = []
    used = []
    check = 0
    for item in list_of_lists:
        for letter in item[0]:
            if letter in used:
                if char.count(letter) == item[0].count(letter):
                    check += 1
                    break
                check = 0
            if letter in char:
                check += 1
                used.append(letter)
        if check == len(item[0]):
            possibles.append(item[0])
            used.clear()

        used.clear()
        check = 0
    return possibles


def scrabble_cheater():
    """The main body of the scrabble cheater responsible for displaying instruction
    asking for user input and displaying  the possible solutions"""
    print()
    print("Welcome to the scrabble word finder this will generate all of the possible words from your scarbble rack "
          "then display them from largest to smallest")
    input_char = input("Please enter all of the available characters ").lower().strip()
    asset = list(input_char)
    print(asset)
    gen_words = find_words(asset)
    print("The possible solutions are")
    gen_words.sort(key=len)
    for word in gen_words:
        print(word)
    gen_more = check_y_or_n("would you like to generate more words [y]es or [n]o? ")
    if gen_more == "y":
        scrabble_cheater()
    else:
        main()


def gen_letters():
    """Generates random letters of the alphabet with added weight placed on the vowels and
    if statement to check if a vowel needs to be added"""
    letters_string = string.ascii_lowercase
    letters = list(letters_string)
    characters = random.choices(letters,
                                weights=[2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1,
                                         1, 1], k=10)
    if "a" not in characters and "e" not in characters and "i" not in characters and "o" not in characters and "u" not in characters:
        characters.remove(characters[0])
        characters.append("a")
    return characters


def quiz_main():
    """Main routine of the quiz responsible for displaying instructions showing the final score
    and asking if the player would like to play again"""
    rand_letters = gen_letters()
    answers = find_words(rand_letters)
    print("definitely not the answers", answers)
    print()
    print("Thank you for choosing to partake in the quiz the rules are as follows")
    print("Only the correct spelling will be accepted")
    print("There are no 1 letter words")
    print("Each letter can only be used as many times as it appears oin your list of words "
          " and each word entered once")
    print("Finally your score is determined by the accumulation of the lengths of words you spell, "
          "for example the word warm would be worth 4 points")
    print("You have as long as you want to obtain the highest score you can when you are finished guessing press [F]")
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
    """Routine that handles of the of guessing from the player and
    checking if the guess is correct, displaying the available letters and giving and
    indication of if the player was correct """
    corr_total = 0
    corr_list = []
    guessed = []
    correct = False
    guess = input("please press enter to begin guessing ")
    while guess != "f":
        print("{} {}".format("the letters you have available to use are ", rand_letters))
        guess = input(
            "please enter you guess and press enter or if you are finished guessing press [f] ").lower().strip()
        for item in answers:
            if guess == item and guess != "f":
                guessed.append(guess)
                answers.remove(item)
                corr_total += len(item)
                corr_list.append(item)
                print("congratulations that was correct ")
                print("{} {} ".format("The total amount of points you have is", corr_total))
                correct = True
        if not correct:
            print("sorry that guess was incorrect please try again")
        correct = False
        print()
        print("{} {}".format("You have previously guessed", guessed))
    print()
    return corr_total, corr_list


def main():
    """Main menu that allows the user to select from 3 different options by calling the respective functions"""
    print()
    print("welcome to the online word guesser:")
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
            choice = check_int("please enter [1, [2] or 3 ")


main()
