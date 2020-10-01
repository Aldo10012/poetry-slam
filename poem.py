import random
from googletrans import Translator

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
    line_num = str(i + 1)
    new_line = poem_list[i]
    poem_list_bakcwards += line_num + ') ' + new_line
    i -= 1

  return poem_list_bakcwards 


# prints poem randomly
def lines_printed_random(file_name):
  poem_list = get_file_lines('poem.txt')
  poem_list_random = ""

  i = 0
  while i < len(poem_list):
    line_num = str(i + 1)
    new_line = random.choice(poem_list)
    poem_list_random += line_num + ') ' + new_line
    i += 1

  return poem_list_random 


# print poem customly
def lines_printed_custom(file_name):
  poem_list = get_file_lines('poem.txt')
  poem_list_custom = ''
  
  line_num = 1
  for lines in poem_list:
    new_line = lines
    translator = Translator()
    translated_sentence = translator.translate(new_line, src='en', dest='es')
    print(str(line_num) + ') ' + str(translated_sentence.text))
    line_num += 1

  return poem_list_custom


# print user's option
def print_users_option():
  prompt = input('Would you like the star spangled banner printed backwards, randomly, or customly: ')
  print(prompt)
  
  if prompt == 'backwards' or prompt == 'Backwards':
    print(lines_printed_backwards('poem.txt'))
  elif prompt == 'randomly' or prompt == 'Randomly':
    print(lines_printed_random('poem.txt'))
  elif prompt == 'customly' or prompt == 'Customly':
    print(lines_printed_custom('poem.txt'))
  else:
    print('Can you repeate that')


print_users_option()
