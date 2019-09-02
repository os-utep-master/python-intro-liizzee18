from Node import Node
import sys    

class Node(object):
  word = ""
  count = -1
  next = None
  def __init__(self, word, count, next):
    self.word = word
    self.count = count
    self.next = next
    
  """
  Reads a words file and generates a dictionary
  based on its contents.
  
  Args:
    words_file: A file object that points to the file with the 
                   words
  
  Returns:
    words_dict: A dictionary with keys as words and values as
                   that word's count
"""
def get_words_dict_from_file(words_file):

    words_dict = dict()
    for line in words_file.readlines():
    #remove new line char
    line = line.strip()
    #convert chars to lowercase 
    line = line.lower()
    line = re.sub('[; : . " , $ # @ |]', '', line)
    line = re.sub("[ ~ , ']" ,' ', line)
    
    words = line.split()
    
    # Considers the case where there is no words, empty line    
    if len(words) == 0:
      continue
    for word in words:
        if word in words_dict:
            words_dict[word] = word_dict[word] +1
        else 
            words_dict[word] = 1
return words_dict



  """
Reads a speech file and generates a linked list without duplicates
  based on its contents
  
  Args:
    words_file: A file object that points to the file with the 
                   words
  
  Returns:
    words_list: A linked list of Node objects

  """
  
  def get_words_list_from_file(words_file):

  words_list = None
  for line in words_file.readlines():
    
    combination = line.split()
    # Considers the case where a username/password entry is incomplete

    helper = words_list
    duplicate = False
    while helper != None:
      if helper.words == combination[1]:
        helper.count = helper.count + 1
        duplicate = True
        break
      helper = helper.next
    if not duplicate:
      words_list = Node(combination[1], 1, words_list)
  return words_list

  """
  Creates a linked list of Node objects based on password dictionary.
  
  Args:
    password_dict: A dictionary with keys are words and values as
                   that word's count
  
  Returns:
    password_list: A linked list of Node objects

  """
def create_list_from_dict(words_dict):
      words_list = None
  for key in words_dict:
    words_list = Node(key, password_dict[key], password_list)
  return words_list

	  """
	  Creates a Python file object based on filename.
	  
	  Args:
	    filename: The name of the file that needs to be read
	  
	  Returns:
	    words_file: A Python file object
	
	  """
def read_from_file(filename):
  words_file  = open(filename, "r")
  return words_file

	  """
	  Sorts a linked list using the bubble sort algorithm.
	  
	  Args:
	    words_list: A linked list of Node objects
	  
	  Returns:
	    sorted_words_list: A linked list of Node objects sorted based on
	                          count
	
	  """
	def bubble_sort(words_list):
        
	  helper = words_list
	  unsorted_words = []
	  unsorted_values =  []
	  while helper != None:
	    unsorted_words.append(helper.words)
	    unsorted_values.append(helper.count)
	    helper = helper.next
	  for value in range(len(unsorted_values)-1,0,-1):
	    for i in range(value):
	      if unsorted_values[i]>unsorted_values[i+1]:
	        temp = unsorted_values[i]
	        unsorted_values[i] = unsorted_values[i+1]
	        unsorted_values[i+1] = temp
	        temp_words = unsorted_words[i]
	        unsorted_words[i] = unsorted_words[i+1]
	        unsorted_words[i+1] = temp_words
	  sorted_words_list = None
	  for value in range(len(unsorted_values)):
	    sorted_words_list = Node(unsorted_words[value], 
	                        unsorted_values[value], sorted_words_list)
	  return sorted_words_list

"""
Reads a words file and generates a linked list without duplicates
  based on its contents
  
  Args:
    words_file: A file object that points to the file with the 
                   words
  
  Returns:
    words_list: A linked list of Node objects

  """
def get_words_list_from_file(words_file):

  words_list = None
  for line in words_file.readlines():
    combination = line.split()
    if len(combination) < 2:
      continue
    helper = words_list
    duplicate = False
    while helper != None:
      if helper.words == combination[1]:
        helper.count = helper.count + 1
        duplicate = True
        break
      helper = helper.next
    if not duplicate:
      words_list = Node(combination[1], 1, password_list)
  return words_list

def main(file1, file2)
    # Files to compare to one another
    words_list1 = get_word_list_from_file(read_from_file(file1))
    words_list2 = create_list_from_dict(words_dict)
    sorted_words_list = bubble_sort(words_list1)
    helper1 = sorted_words_list
    
    print("The words appearance :")
    for _ in range(20):
        print(helper1.word + ": " + str(helper1.count))
        helper1 = helper1.next
        sorted_words_list = None



    
main()
