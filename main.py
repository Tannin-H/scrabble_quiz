my_file = open("words", "r")

list_of_lists = []
potentials = []
char = []
for line in my_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(line_list)

my_file.close()
"""def find_words():
  for list in list_of_lists:
    if len(list[0]) <= num_char:
      potentials.append(list)

  for item in potentials:
    for letter in len(item[0]):
      if letter == char[0] and letter == char[1] and letter == char[3]:
        print(item)


num_char = int(input("please enter how many letters you have available to use "))

for num in range(0, num_char):
  input_char = input("please enter one of the characters you have available to use ")
  char.append(input_char)

find_words()"""
def menu():
  print("welcome to the online word guesser")
  print("you will be letters from the alphabet and you have to see how many words you can make")
  print("if you would like to take part in the quiz press [1]")
  print("if you would like to use the scrabble cheater press [2]")
  choice = input("please enter [1 or [2] ")

menu()
