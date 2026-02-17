def count_characters(sentence): #this function counts the characters in the sentence with spaces
    count=0 # initializing variable
    for character in sentence: #checks the characters in the sentence and increaments charater by 1
        count+=1 # increments count as per the number of characters
    return count

def count_words(sentence):#this splits the sentence into a list of strings
    return len(sentence.split()) # this gives the length of the newly created string

def count_unique_words(sentence):
    words = sentence.split() # Wors will have a list of words
    normalized = [w.lower() for w in words] # each word is now converted to lower case and added as a list
    return len(set(normalized)) # the set function is used to give back unique elements in a list and this gives the lenght of the lower case list

def longest_word(sentence):
    words = sentence.split() # the first word is taken as default and compared with the others and printed.
    if not words:
        return ""
    longest = words[0]
    for w in words[1:]:
        if len(w) > len(longest):
            longest = w
    return longest

while True:
    input_sentence=str(input("Enter a sentence: "))
    while len(input_sentence)<2:
        if input_sentence == "" or input_sentence == " ":
            input_sentence= str(input("Please enter the sentence again: "))
        else:
            break
    menu=int(input("1 → Number of characters (including spaces)\n2 → Number of words \n3 → Number of unique words \n4 → Longest word \n5 → Show everything (all four)\nEnter 6 to exit the program.\nWhat do you want to do with the sentence? "))
    if menu == 0 or menu> 6:
        menu=input("Please enter a valid number")
    if menu==1: #this executes function to count strings
        print("Number of characters: "+ str(count_characters(input_sentence)))
    if menu==2:
        print("Number of words: "+str(count_words(input_sentence)))
    if menu==3:
        print("Number of Unique words: "+str(count_unique_words(input_sentence)))
    if menu == 4:
        print("Longest word is: "+str(longest_word(input_sentence)))
    if menu == 5:
        print("Number of characters: "+ str(count_characters(input_sentence)))
        print("Number of words: "+str(count_words(input_sentence)))
        print("Number of unique words: "+str(count_unique_words(input_sentence)))
        print("Longest word is: "+str(longest_word(input_sentence)))
    if menu==6:
        break


    
    



    
    
