# ISSUE
#python3 searchlist.py 0bt 1gr 2gi 3gt 4ge
#['0bt', '1gr', '2gi', '3gt', '4ge']
#Green letters list: ['r', 'i', 't', 'e']
#Possible words: ['trite', 'write']
#TRITE should be eliminated based on the first t being black

# I've fixed a bug that eliminated words that had a second occurrence of a letter (wordle has a quirk where a letter can be green and black for the same letter in a given word)

import sys

file = open('wordlelist', 'r')
read_data = file.read()
word_list = read_data.split() #All of the words in the word list file are put into word_list

arg_list = [] #All of the command line args will be put into this list
result_list = [] #Words not eliminated will be stored in this list
green_letters = [] #A green letter can appear black in certain circumstances. Need a way to mitigate for this

# Remove the first arg, we don't need the file name
sys.argv.remove('searchlist.py')

# Put the command line args into a list
for arg in sys.argv:
    arg_list.append(arg)
    if arg[1] == 'g': # If it's a green letter arg, add the letter to the green_letters list
        green_letters.append(arg[2])

print(arg_list)

for w in word_list: # Go through every word in the word list

    flag = 0 # We'll default to 0 for words to keep, set to -1 for words to reject
    
    # Use this block to debug if issues are encountered
    #if w == "SOME_TEST_WORD":
    #    print(f"SOME_TEST_WORD. Flag = {flag}")


    for entry in arg_list: #Examine the current word against the args in arg_list
        
        if entry[1] == 'y': # if y is in the entry at index[1] it's a yellow letter
            yellow_letter_index = int(entry[0]) # cast the char at index 0 to an int
            
            if w.find(entry[2]) == -1:  #We want to reject words that do not contain the yellow letter. Search the current word (w) for the yellow letter, if w does not contain the yellow letter
                flag = -1 # Give it the -1 flag for rejection
                
            if w[yellow_letter_index] == entry[2]: # We also want to reject words that have the yellow letter in the same position as where we found it before
                flag = -1 # Give it the -1 flag for rejection
                      
        
        if entry[1] == 'g': # if g is in the entry at index[1] it's a green letter
            green_letter_index = int(entry[0])  # cast the char at index 0 to an int
            
            if w[green_letter_index] != entry[2]: # We want to reject words that do not have the green letter at this particular index
                flag = -1 # Give it the -1 flag for rejection
                       
        if entry[1] == 'b':  # Black letter filtering
            black_letter = entry[2]
            black_index = int(entry[0])  # Position of the black letter

            if black_letter in w:  # If the black letter exists in the word
                if black_letter not in green_letters:  
                    flag = -1  # Reject if the letter shouldn't be in the word at all
                elif w[black_index] == black_letter:  
                    flag = -1  # Reject if the letter appears in the same position as black                  
    
    if flag != -1: #after all of the above logic, if the word is not rejected, append it to the result_list
        result_list.append(w)

#Print the green_letters list for debug if necessary
#print(f"Green letters list: {green_letters}")
print(f"Possible words: {result_list}")
file.close()


