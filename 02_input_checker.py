# Checks user choice is "integer", "text" or "image"
from cgitb import text
from email.mime import image


def user_choice():

    valid = false
    while not valid:

        response = "File type (integer / text / image): ". lower(), text(), image()

        if response == "text" or response == "t":
            return response

        else:
            print("PLease choose a valid file type!")
            print()