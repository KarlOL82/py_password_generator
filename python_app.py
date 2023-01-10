import string
import random

characters = (string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How many characters would you like in your password?"))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)


    password = "".join(password)

    print(password)

option = input("Do you want to generate a password? (Yes/No): ")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Program ended")
    quit()
else:
    print("Invalid input, please input Yes or No")
    quit()