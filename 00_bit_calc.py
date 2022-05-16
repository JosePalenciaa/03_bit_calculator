# Functions go here


# Puts series of symbols at start and end of text (for emphasis)
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

# Checks users choice is an integer
def num_check(question, low):
    valid = False
    while not valid:
        
        error = "Please enter a number that is more than zero."
       "" 
        try:
        
            # ask user to enter a number
            response = int(input(question))
            
            # checks number is more than zero
            if response >= low:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    
    
# Main routine goes here
statement_generator("Look Stars!", "☆ ")

# Heading
statement_generator("Bit Calculator for Integers, Text & Images", "★ ")

# Display instructions if user has not used the program before

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":
    
    data_type = user_choice()
    print("You successfully chosen", data_type)
    if data_type =="integer":
        var_integer = num_check("Enter an Integer: ", 0)