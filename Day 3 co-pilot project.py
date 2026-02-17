import random
def get_valid_input(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
            if 1 <= number <= 50:
                return number
            else:
                number=int(input(("Number entered outside range. Please enter a number in range: ")))
                get_valid_input(number)
                return number
        except ValueError:
            print("Invalid input.")

random_number = random.randint(1, 51)
print("Hey User, Let's play a game!\nI'm thinking of a number between 1 and 50.\nYou have 7 attempts to guess correctly.\nLet's start!")
number = get_valid_input("Enter a number: ")
attempt = 0
while attempt <=7:
    if attempt ==7:
        print("You have exhausted your attempts. Better luck next time :D")
        break
    if number > random_number:
        number= get_valid_input("Try lower! Enter a number: ")
    elif number < random_number:
        number=get_valid_input("Try Higher! Enter a number: ")
    else:
        print("Correct!")
        break
    attempt +=1

    
            
            


