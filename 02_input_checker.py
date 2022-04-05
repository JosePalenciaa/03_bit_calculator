# Checks user choice is "integer", "text" or "image"
from cgitb import text
from email.mime import image

def user_choice():

    valid = False
    while not valid:

        response = input("File type (integer / text / image): "). lower()

        text_ok = ["text","t","txt"]
        if response == "text" or response == "t":
            return "text"

        else:
            print("PLease choose a valid file type!")
            print()

# Main routine goes here
data_type = user_choice()
print("You successfully chosen", data_type)

print()