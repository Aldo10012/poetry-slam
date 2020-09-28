import random

#gets the lines and puts them in a list
def get_file_lines(file_name):
    with open('poem.txt', 'r') as f:
      poem = f.readlines()
      poem_list = []

      for i in poem:
        poem_list.append(i) 
      return poem_list


# gets lines and prints them backwards
def lines_printed_backwards(file_name):
  poem_list = get_file_lines('poem.txt')
  poem_list_bakcwards = ""
  
  i = len(poem_list)-1
  while i > -1:
    new_line = poem_list[i]
    poem_list_bakcwards += new_line
    i -= 1

  return poem_list_bakcwards 


# prints poem randomly
def lines_printed_random(file_name):
  poem_list = get_file_lines('poem.txt')
  poem_list_random = ""

  i = 0
  while i < len(poem_list):
    new_line = random.choice(poem_list)
    poem_list_random += new_line
    i += 1

  return poem_list_random 





print(get_file_lines('poem.txt'))
print('\n')
print(lines_printed_backwards('poem.txt'))
print('\n')
print(lines_printed_random('poem.txt'))