def check_string(input_string):# Checks if string is empty
    while not input_string.strip(): # This strips blank spaces, if this is not possible then the string is empty
        input_string= str(input("Invalid input; The string is empty. Please enter a string properly: "))
    return input_string
        
def reverse_sentence(input_string):#reverses the string
    split_string=input_string.split()#splits the string into list
    split_string.reverse()#reverses the list
    return(" ".join(split_string))#joins the list into a string again

def word_frequency(input_string):# Declaration of function
    split_string=input_string.lower().split()#converts the sentence into lowercase
    wordlist= list(set(split_string))#creates a non-repeating set(sets are non repeating)
    word_frequency_list={}#declaration of dictionary
    frequency_list=[] #frequency list declaration for merging into dictionary
    frequency=0 #variable declaration
    for i in wordlist:
        frequency=0
        for j in split_string:
            if i==j:
                frequency+=1
        frequency_list.append(frequency) #appends into the frequency list per order.
    word_frequency_list=dict(zip(wordlist,frequency_list))
    return word_frequency_list

def replace_word(input_string, input_word, replace_word):
    split_string=input_string.split()
    if input_word in split_string:
        index=split_string.index(input_word)
        split_string.pop(index)
        split_string.insert(index, replace_word)
    print(" ".join(split_string))
    
while True:
    input_sentence=check_string(str(input("Enter a sentence: ")))#String from user
    menu=int(input("1 → Reverse Sentence \n2 → Show word frequency\n3 → Replace a word \n4 → Exit \nWhat do you want to do with the sentence? "))
    if menu <1 or menu> 4: # invalid menu number check
        menu=input("Please enter a valid number")
    if menu==1: 
        print("Reversed String: "+ str(reverse_sentence(input_sentence)))
    if menu==2: 
        print("Word frequency for each word: "+str(word_frequency(input_sentence)))
    if menu==3:
        replacefor=check_string(str(input("Enter the word you want to replace for: ")))
        while replacefor not in input_sentence.split():
            replacefor=check_string(str(input("Word not present in sentence. Please enter the word you want to replace for: ")))
        replacewith=check_string(str(input("Enter the word you want to replace with: ")))
        replace_word(input_sentence, replacefor, replacewith)
    if menu == 4:
        print("Program terminated. Thank you for your inputs.")
        break


    
    


    
    
