# Functions go here


# Puts series of symbols at start and end of text (for emphasis)
from tkinter.colorchooser import askcolor


def statement_generator(text, decoration):

    #Makes string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# Checks user choice is 'integer', 'text' or 'image'
def user_choice():

    # Responses
    text_ok = ["text","t","txt"]
    integer_ok = ["int","integer","number", "#"]
    image_ok = ["image","img","picture", "pix", "pic", "p"]

    valid = False
    while not valid:
        
        # Asks users for choice and change rsponse to lowercase
        response = input("File type (integer / text / image): "). lower()

        # Checks for valid response and returns text, integer, image
        
        if response in text_ok:
            return "text"

        elif response in integer_ok:
            return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for an image: ")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            # if response is not valid, output an error
            print("Please choose a valid file type!")
            print()


# Main routine goes here
statement_generator("Look Stars!", "☆ ")

# Heading
statement_generator("Bit Calculator for Integers, Text & Images", "-")

# Display instructions if user has not used the program before

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":
    
    data_type = user_choice()
    print("You successfully chosen", data_type)