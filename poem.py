def get_file_lines(file_name):
    with open('poem.txt', 'r') as f:
      poem = f.readlines()
      poem_str = ""

      for i in poem:
        poem_str += i 
    
      return poem_str


# def lines_printed_backwards() {

# }

# def lines_printed_random() {

# }

# def lines_printed_custom() {

# }
print('Printing poem normaly')
print(get_file_lines('poem.txt'))
print('\n')
